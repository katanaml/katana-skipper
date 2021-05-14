from .worker import app
from .backend.event_producer import EventProducer
from celery.utils.log import get_task_logger
import json

# Create logger - enable to display messages on task logger
celery_log = get_task_logger(__name__)


@app.task(name='api.process_workflow')
def process_workflow(task_type, data):
    event_producer = EventProducer()
    response = event_producer.call(data)
    response_json = json.loads(response)

    celery_log.info(task_type + " task completed")
    return response_json
