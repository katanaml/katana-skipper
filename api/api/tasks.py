from .worker import app
from skipper_lib.events.event_producer import EventProducer
from celery.utils.log import get_task_logger
import json
import requests

# Create logger - enable to display messages on task logger
celery_log = get_task_logger(__name__)


@app.task(name='api.process_workflow')
def process_workflow(payload):
    payload_json = json.loads(payload)
    task_type = payload_json['task_type']

    param = task_type + '_async'
    r = requests.get('http://127.0.0.1:5000/api/v1/skipper/workflow/' + param)
    queue_name = r.json()['queue_name']

    if queue_name is '-':
        return

    event_producer = EventProducer(username='skipper',
                                   password='welcome1',
                                   host='localhost',
                                   port=5672,
                                   service_name='api_async',
                                   logger='http://127.0.0.1:5001/api/v1/skipper/logger/log_producer')
    response = event_producer.call(queue_name, payload)
    response_json = json.loads(response)

    celery_log.info(task_type + " task completed")
    return response_json
