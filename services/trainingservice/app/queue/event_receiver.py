import pika
import json
from app.training_service import TrainingService


class EventReceiver(object):
    def __init__(self):
        credentials = pika.PlainCredentials('skipper', 'welcome1')
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost',
                                                                       port=5672,
                                                                       credentials=credentials))

        channel = connection.channel()
        channel.queue_declare(queue='skipper_training')

        channel.basic_qos(prefetch_count=1)
        channel.basic_consume(queue='skipper_training', on_message_callback=self.on_request)

        print("Awaiting requests for [x] training service [x]")
        channel.start_consuming()


    def on_request(self, ch, method, props, body):
        body_json = json.loads(body)

        training_service = TrainingService()
        res = training_service.call(body_json)

        payload = {
            'result': res
        }
        response = json.dumps(payload, indent=4)

        ch.basic_publish(exchange='',
                         routing_key=props.reply_to,
                         properties=pika.BasicProperties(correlation_id=props.correlation_id),
                         body=response)
        ch.basic_ack(delivery_tag=method.delivery_tag)

        print('Processed request:', body_json['task_type'])