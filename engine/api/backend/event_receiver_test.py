import pika
import json

credentials = pika.PlainCredentials('skipper', 'welcome1')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost',
                                                               port=5672,
                                                               credentials=credentials))
channel = connection.channel()
channel.queue_declare(queue='skipper_web_api')


def on_request(ch, method, props, body):
    payload = {
        'result': 'TASK_COMPLETED'
    }
    response = json.dumps(payload, indent=4)

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id=props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)

    body_json = json.loads(body)
    print('Processed request:', body_json['task_type'])


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='skipper_web_api', on_message_callback=on_request)

print(" [x] Awaiting requests")
channel.start_consuming()
