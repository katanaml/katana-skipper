from .worker import app
from skipper_lib.events.event_producer import EventProducer
from celery.utils.log import get_task_logger
import json
import skipper_lib.workflow.workflow_helper as workflow_helper
import os

# Create logger - enable to display messages on task logger
celery_log = get_task_logger(__name__)


@app.task(name='api.process_workflow')
def process_workflow(payload):
    payload_json = json.loads(payload)
    task_type = payload_json['task_type']

    queue_name = workflow_helper.call(task_type,
                                      os.getenv('WORKFLOW_URL',
                                                'http://127.0.0.1:5000/api/v1/skipper/workflow/'),
                                      '_async')

    if queue_name is '-':
        return

    event_producer = EventProducer(username=os.getenv('RABBITMQ_USER', 'skipper'),
                                   password=os.getenv('RABBITMQ_PASSWORD', 'welcome1'),
                                   host=os.getenv('RABBITMQ_HOST', '127.0.0.1'),
                                   port=os.getenv('RABBITMQ_PORT', 5672),
                                   service_name='api_async',
                                   logger=os.getenv('LOGGER_PRODUCER_URL',
                                                    'http://127.0.0.1:5001/api/v1/skipper/logger/log_producer'))
    response = event_producer.call(queue_name, payload)
    response_json = json.loads(response)

    celery_log.info(task_type + " task completed")
    return response_json
