from fastapi import APIRouter
from ..models import WorkflowTaskResult, WorkflowTaskCancelled
from ..models import WorkflowTaskDataMobileNet
from ..dependencies import sync_request_helper

router = APIRouter(
    prefix='/mobilenet',
    tags=['mobilenet']
)


@router.post('/execute_sync', response_model=WorkflowTaskResult, status_code=202,
             responses={202: {'model': WorkflowTaskCancelled, 'description': 'Accepted: Not Ready'}})
def exec_workflow_task_mobilenet_sync(workflow_task_data: WorkflowTaskDataMobileNet):
    response = sync_request_helper(workflow_task_data)

    return {'task_id': '-',
            'task_status': 'Success',
            'outcome': str(response)}
