import pika
import uuid
import requests


class EventProducer(object):
    def __init__(self, username, password, host, port, service_name, logger):
        self.service_name = service_name
        self.logger = logger
        self.credentials = pika.PlainCredentials(username, password)
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=host,
                                                                            port=port,
                                                                            credentials=self.credentials))
        self.channel = self.connection.channel()

        result = self.channel.queue_declare(queue='', exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True
        )

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, queue_name, payload):
        self.response = None
        self.corr_id = str(uuid.uuid4())

        if self.logger is not None:
            params = {"correlation_id": self.corr_id,
                      "queue_name": queue_name,
                      "service_name": self.service_name,
                      "task_type": 'start'
                      }
            try:
                requests.post(self.logger, json=params)
            except requests.exceptions.RequestException as e:
                print('Logger service is not available')

        self.channel.basic_publish(
            exchange='',
            routing_key=queue_name,
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id
            ),
            body=payload
        )

        while self.response is None:
            self.connection.process_data_events()

        if self.logger is not None:
            params = {"correlation_id": self.corr_id,
                      "queue_name": queue_name,
                      "service_name": self.service_name,
                      "task_type": 'end'
                      }
            try:
                requests.post(self.logger, json=params)
            except requests.exceptions.RequestException as e:
                print('Logger service is not available')

        return self.response
