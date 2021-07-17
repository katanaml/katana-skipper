from fastapi import APIRouter
from .models import WorkflowTask, WorkflowTaskResult, WorkflowTaskData, WorkflowTaskCancelled
from .tasks import process_workflow
from celery.result import AsyncResult
from fastapi.responses import JSONResponse
import json
from skipper_lib.events.event_producer import EventProducer
import skipper_lib.workflow.workflow_helper as workflow_helper
import os

router_tasks = APIRouter()


@router_tasks.get('/')
def touch():
    return 'API is running'


@router_tasks.post('/execute_async', response_model=WorkflowTask, status_code=202)
def exec_workflow_task_async(workflow_task_data: WorkflowTaskData):
    payload = workflow_task_data.json()

    task_id = process_workflow.delay(payload)

    return {'task_id': str(task_id),
            'task_status': 'Processing'}


@router_tasks.get('/{task_id}', response_model=WorkflowTaskResult, status_code=202,
                  responses={202: {'model': WorkflowTask, 'description': 'Accepted: Not Ready'}})
async def exec_workflow_task_result(task_id):
    task = AsyncResult(task_id)
    if not task.ready():
        return JSONResponse(status_code=202,
                            content={'task_id': str(task_id),
                                     'task_status': 'Processing'})
    result = task.get()
    return {'task_id': task_id,
            'task_status': 'Success',
            'outcome': str(result)}


@router_tasks.post('/execute_sync', response_model=WorkflowTaskResult, status_code=202,
                   responses={202: {'model': WorkflowTaskCancelled, 'description': 'Accepted: Not Ready'}})
def exec_workflow_task_sync(workflow_task_data: WorkflowTaskData):
    payload = workflow_task_data.json()

    queue_name = workflow_helper.call(workflow_task_data.task_type,
                                      os.getenv('WORKFLOW_URL'),
                                      '_sync')

    if queue_name is '-':
        return JSONResponse(status_code=202,
                            content={'task_id': '-',
                                     'task_status': 'Wrong task type'})

    event_producer = EventProducer(username=os.getenv('RABBITMQ_USER'),
                                   password=os.getenv('RABBITMQ_PASSWORD'),
                                   host=os.getenv('RABBITMQ_HOST'),
                                   port=os.getenv('RABBITMQ_PORT'),
                                   service_name='api_sync',
                                   logger=os.getenv('LOGGER_PRODUCER_URL'))
    response = json.loads(event_producer.call(queue_name, payload))

    return {'task_id': '-',
            'task_status': 'Success',
            'outcome': str(response)}
