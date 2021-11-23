from fastapi import APIRouter
from ..models import WorkflowTask, WorkflowTaskResult, WorkflowTaskCancelled
from ..models import WorkflowTaskDataTraining, WorkflowTaskDataPredict
from ..tasks import process_workflow
from ..dependencies import sync_request_helper
from celery.result import AsyncResult
from fastapi.responses import JSONResponse

router = APIRouter(
    prefix='/boston',
    tags=['boston']
)


@router.post('/task_training', response_model=WorkflowTask, status_code=202)
def task_training(workflow_task_data: WorkflowTaskDataTraining):
    payload = workflow_task_data.json()

    task_id = process_workflow.delay(payload)

    return {'task_id': str(task_id),
            'task_status': 'Processing'}


@router.get('/{task_id}', response_model=WorkflowTaskResult, status_code=202,
            responses={202: {'model': WorkflowTask, 'description': 'Accepted: Not Ready'}})
async def task_status(task_id):
    task = AsyncResult(task_id)
    if not task.ready():
        return JSONResponse(status_code=202,
                            content={'task_id': str(task_id),
                                     'task_status': 'Processing'})
    result = task.get()
    return {'task_id': task_id,
            'task_status': 'Success',
            'outcome': str(result)}


@router.post('/task_predict', response_model=WorkflowTaskResult, status_code=202,
             responses={202: {'model': WorkflowTaskCancelled, 'description': 'Accepted: Not Ready'}})
def task_predict(workflow_task_data: WorkflowTaskDataPredict):
    response = sync_request_helper(workflow_task_data)

    return {'task_id': '-',
            'task_status': 'Success',
            'outcome': str(response)}
