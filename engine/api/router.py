from fastapi import APIRouter
from .models import WorkflowTask, WorkflowTaskResult, WorkflowTaskData
from .tasks import process_workflow
from celery.result import AsyncResult
from fastapi.responses import JSONResponse

router_tasks = APIRouter()


@router_tasks.get('/')
def touch():
    return 'API is running'


@router_tasks.post('/start', response_model=WorkflowTask, status_code=202)
async def start_workflow_task(workflow_task_data: WorkflowTaskData):
    task_id = process_workflow.delay(workflow_task_data.task_type,
                                     workflow_task_data.payload,
                                     workflow_task_data.description)
    return {'task_id': str(task_id),
            'task_status': 'Processing'}


@router_tasks.get('/result/{task_id}', response_model=WorkflowTaskResult, status_code=202,
                  responses={202: {'model': WorkflowTask, 'description': 'Accepted: Not Ready'}})
async def workflow_task_result(task_id):
    task = AsyncResult(task_id)
    if not task.ready():
        return JSONResponse(status_code=202,
                            content={'task_id': str(task_id),
                                     'task_status': 'Processing'})
    result = task.get()
    return {'task_id': task_id,
            'task_status': 'Success',
            'outcome': str(result)}
