from fastapi import APIRouter
from fastapi import BackgroundTasks
from .models import LogTask
from .models import LogProducer
from .models import LogReceiver
from .models import LogWorkflow
from .logger import print_producer
from .logger import print_receiver
from .logger import print_workflow

router_logger = APIRouter()


@router_logger.get('/')
def touch():
    return 'API is running'


@router_logger.post('/log_producer', response_model=LogTask, status_code=202)
def exec_log_producer(logger_data: LogProducer, background_tasks: BackgroundTasks):
    background_tasks.add_task(print_producer, logger_data)

    return {'status': 'logged'}


@router_logger.post('/log_receiver', response_model=LogTask, status_code=202)
def exec_log_receiver(logger_data: LogReceiver, background_tasks: BackgroundTasks):
    background_tasks.add_task(print_receiver, logger_data)

    return {'status': 'logged'}


@router_logger.post('/log_workflow', response_model=LogTask, status_code=202)
def exec_log_workflow(logger_data: LogWorkflow, background_tasks: BackgroundTasks):
    background_tasks.add_task(print_workflow, logger_data)

    return {'status': 'logged'}
