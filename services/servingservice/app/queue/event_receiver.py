import pika
from app.serving_service import ServingService


class EventReceiver(object):
    def __init__(self):
        credentials = pika.PlainCredentials('skipper', 'welcome1')
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost',
                                                                       port=5672,
                                                                       credentials=credentials))

        channel = connection.channel()
        channel.queue_declare(queue='skipper_serving')

        channel.basic_qos(prefetch_count=1)
        channel.basic_consume(queue='skipper_serving', on_message_callback=self.on_request)

        print("Awaiting requests for [x] serving service [x]")
        channel.start_consuming()

    def on_request(self, ch, method, props, body):
        serving_service = ServingService()
        response, task_type = serving_service.call(body)

        ch.basic_publish(exchange='',
                         routing_key=props.reply_to,
                         properties=pika.BasicProperties(correlation_id=props.correlation_id),
                         body=response)
        ch.basic_ack(delivery_tag=method.delivery_tag)

        print('Processed request:', task_type)
