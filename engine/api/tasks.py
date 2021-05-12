from .worker import app
from celery.utils.log import get_task_logger

# Create logger - enable to display messages on task logger
celery_log = get_task_logger(__name__)


@app.task(name='api.process_workflow')
def process_workflow(task_type, payload, description):


    celery_log.info(task_type + " task completed!")
    return 'OK'
