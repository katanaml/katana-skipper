from .worker import app
from skipper_lib.events.event_producer import EventProducer
from celery.utils.log import get_task_logger
import json

# Create logger - enable to display messages on task logger
celery_log = get_task_logger(__name__)


@app.task(name='api.process_workflow')
def process_workflow(payload):
    payload_json = json.loads(payload)
    task_type = payload_json['task_type']

    queue_name = None
    if task_type == 'training':
        queue_name = 'skipper_training'
    elif task_type == 'inference':
        queue_name = 'skipper_inference'

    if queue_name is None:
        return

    event_producer = EventProducer(username='skipper', password='welcome1', host='localhost', port=5672)
    response = event_producer.call(queue_name, payload)
    response_json = json.loads(response)

    celery_log.info(task_type + " task completed")
    return response_json
