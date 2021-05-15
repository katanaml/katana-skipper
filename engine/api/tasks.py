from .worker import app
from .backend.event_producer import EventProducer
from celery.utils.log import get_task_logger
import json

# Create logger - enable to display messages on task logger
celery_log = get_task_logger(__name__)


@app.task(name='api.process_workflow')
def process_workflow(task_type, data):
    queue_name = None
    if task_type == 'training':
        queue_name = 'skipper_training'
    elif task_type == 'inference':
        queue_name = 'skipper_inference'

    event_producer = EventProducer()
    response = event_producer.call(queue_name, data)
    response_json = json.loads(response)

    celery_log.info(task_type + " task completed")
    return response_json
