import pika
import uuid
import requests
from pika.exceptions import ChannelClosedByBroker


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

        try:
            queue_state = self.channel.queue_declare('skipper_mobilenet', passive=True, durable=True)
            if queue_state.method.consumer_count == 0:
                self.logger_helper(self.corr_id, queue_name, self.service_name, self.logger, 'start',
                                   'No subscriber available')
                return 'No subscriber available'
        except Exception as e:
            self.logger_helper(self.corr_id, queue_name, self.service_name, self.logger, 'start',
                               'No subscriber available')
            return 'No subscriber available'

        self.logger_helper(self.corr_id, queue_name, self.service_name, self.logger, 'start', '-')

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

        self.logger_helper(self.corr_id, queue_name, self.service_name, self.logger, 'end', '-')

        return self.response

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
