from fastapi import APIRouter
from .models import LogTask
from .models import LogProducer
from .models import LogReceiver
from .logger import print_producer
from .logger import print_receiver

router_logger = APIRouter()


@router_logger.get('/')
def touch():
    return 'API is running'


@router_logger.post('/log_producer', response_model=LogTask, status_code=202)
def exec_log_producer(logger_data: LogProducer):
    print_producer(logger_data)

    return {'status': 'logged'}


@router_logger.post('/log_receiver', response_model=LogTask, status_code=202)
def exec_log_receiver(logger_data: LogReceiver):
    print_receiver(logger_data)

    return {'status': 'logged'}
