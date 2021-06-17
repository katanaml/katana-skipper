from fastapi import APIRouter
from .models import ServiceInfo
from .workflow import get_queue_name

router_workflow = APIRouter()


@router_workflow.get('/')
def touch():
    return 'API is running'


@router_workflow.get('/{service_id}', response_model=ServiceInfo, status_code=202)
def exec_workflow_queue_name(service_id):
    queue_name = get_queue_name(service_id)

    return {'service_id': service_id,
            'queue_name': queue_name}
