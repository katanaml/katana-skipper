import pika
import requests
import json


class EventReceiver(object):
    def __init__(self, username, password, host, port, queue_name, service, service_name, logger):
        self.service_worker = service
        self.service_name = service_name
        self.queue_name = queue_name
        self.logger = logger

        credentials = pika.PlainCredentials(username, password)
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=host,
                                                                       port=port,
                                                                       credentials=credentials))

        channel = connection.channel()
        channel.queue_declare(queue=queue_name)

        channel.basic_qos(prefetch_count=1)
        channel.basic_consume(queue=queue_name, on_message_callback=self.on_request)

        print("Awaiting requests from [x] " + queue_name + " [x]")
        channel.start_consuming()

    def on_request(self, ch, method, props, body):
        service_instance = self.service_worker()

        self.logger_helper(props.correlation_id, self.queue_name, self.service_name, self.logger, 'start', '-')

        try:
            response, task_type = service_instance.call(body)

            ch.basic_publish(exchange='',
                             routing_key=props.reply_to,
                             properties=pika.BasicProperties(correlation_id=props.correlation_id),
                             body=response)
            ch.basic_ack(delivery_tag=method.delivery_tag)

            self.logger_helper(props.correlation_id, self.queue_name, self.service_name, self.logger, 'end', '-')

            print('Processed request:', task_type)
        except Exception as e:
            response = {"error": 'Receiver exception',
                        "queue": self.queue_name,
                        "service_name": self.service_name,
                        "correlation_id": props.correlation_id
                        }
            result = json.dumps(response)

            self.logger_helper(props.correlation_id, self.queue_name, self.service_name, self.logger, 'end', 'Receiver exception')
            print('Receiver exception')

            ch.basic_publish(exchange='',
                             routing_key=props.reply_to,
                             properties=pika.BasicProperties(correlation_id=props.correlation_id),
                             body=result)
            ch.basic_ack(delivery_tag=method.delivery_tag)

    def logger_helper(self, corr_id, queue_name, service_name, logger, task_type, description):
        if self.logger is not None:
            params = {"correlation_id": corr_id,
                      "queue_name": queue_name,
                      "service_name": service_name,
                      "task_type": task_type,
                      "description": description
                      }
            try:
                requests.post(logger, json=params)
            except requests.exceptions.RequestException as e:
                print('Logger service is not available')
