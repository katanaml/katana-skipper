from fastapi.responses import JSONResponse
import json
from skipper_lib.events.event_producer import EventProducer
import skipper_lib.workflow.workflow_helper as workflow_helper
import os


def sync_request_helper(workflow_task_data):
    payload = workflow_task_data.json()

    queue_name = workflow_helper.call(workflow_task_data.task_type,
                                      os.getenv('WORKFLOW_URL',
                                                'http://127.0.0.1:5000/api/v1/skipper/workflow/'),
                                      '_sync')

    if queue_name is '-':
        return JSONResponse(status_code=202,
                            content={'task_id': '-',
                                     'task_status': 'Wrong task type'})

    event_producer = EventProducer(username=os.getenv('RABBITMQ_USER', 'skipper'),
                                   password=os.getenv('RABBITMQ_PASSWORD', 'welcome1'),
                                   host=os.getenv('RABBITMQ_HOST', '127.0.0.1'),
                                   port=os.getenv('RABBITMQ_PORT', 5672),
                                   service_name='api_sync',
                                   logger=os.getenv('LOGGER_PRODUCER_URL',
                                                    'http://127.0.0.1:5001/api/v1/skipper/logger/log_producer'))
    response = json.loads(event_producer.call(queue_name, payload))

    return response
