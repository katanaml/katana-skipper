from .models import LogProducer
from .models import LogReceiver
from .models import LogWorkflow
import time


def print_producer(logger_data: LogProducer):
    print()
    print('Event type: producer')
    print('Correlation ID:', logger_data.correlation_id)
    print('Queue name:', logger_data.queue_name)
    print('Service name:', logger_data.service_name)
    print('Task type:', logger_data.task_type)
    print('Description:', logger_data.description)
    print('Timestamp:', time.time())
    print()


def print_receiver(logger_data: LogReceiver):
    print()
    print('Event type: receiver')
    print('Correlation ID:', logger_data.correlation_id)
    print('Queue name:', logger_data.queue_name)
    print('Service name:', logger_data.service_name)
    print('Task type:', logger_data.task_type)
    print('Description:', logger_data.description)
    print('Timestamp:', time.time())
    print()


def print_workflow(logger_data: LogWorkflow):
    print()
    print('Event type: workflow')
    print('Service ID:', logger_data.service_id)
    print('Queue name:', logger_data.queue_name)
    print('Timestamp:', time.time())
    print()
