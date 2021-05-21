import pika
from app.data_service import DataService


class EventReceiver(object):
    def __init__(self):
        credentials = pika.PlainCredentials('skipper', 'welcome1')
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost',
                                                                       port=5672,
                                                                       credentials=credentials))

        channel = connection.channel()
        channel.queue_declare(queue='skipper_data')

        channel.basic_qos(prefetch_count=1)
        channel.basic_consume(queue='skipper_data', on_message_callback=self.on_request)

        print("Awaiting requests for [x] data service [x]")
        channel.start_consuming()

    def on_request(self, ch, method, props, body):
        data_service = DataService()
        response, task_type = data_service.call(body)

        ch.basic_publish(exchange='',
                         routing_key=props.reply_to,
                         properties=pika.BasicProperties(correlation_id=props.correlation_id),
                         body=response)
        ch.basic_ack(delivery_tag=method.delivery_tag)

        print('Processed request:', task_type)
