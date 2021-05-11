from fastapi import APIRouter
from .models import WorkflowTask, WorkflowTaskResult

router_tasks = APIRouter()


@router_tasks.get('/')
def touch():
    return 'API is running'


@router_tasks.post('/start', response_model=WorkflowTask, status_code=202)
async def start_workflow_task():
    return {'task_id': '12345', 'task_status': 'Processing'}


@router_tasks.get('/result/{task_id}', response_model=WorkflowTaskResult, status_code=202,
                  responses={202: {'model': WorkflowTask, 'description': 'Accepted: Not Ready'}})
async def workflow_task_result(task_id):
    return {'task_id': task_id, 'task_status': 'Done'}
