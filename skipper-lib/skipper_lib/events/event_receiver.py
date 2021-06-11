import pika


class EventReceiver(object):
    def __init__(self, username, password, host, port, queue_name, service):
        self.service_worker = service

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
        response, task_type = service_instance.call(body)

        ch.basic_publish(exchange='',
                         routing_key=props.reply_to,
                         properties=pika.BasicProperties(correlation_id=props.correlation_id),
                         body=response)
        ch.basic_ack(delivery_tag=method.delivery_tag)

        print('Processed request:', task_type)
