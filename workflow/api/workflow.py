import json
import skipper_lib.logger.logger_helper as logger_helper
import os


def get_queue_name(service_id):
    f = open('./api/workflow.json')
    data = json.load(f)

    queue_name = '-'
    for x in data:
        for key, value in x.items():
            if key == service_id:
                queue_name = value

    f.close()

    params = {"service_id": service_id,
              "queue_name": queue_name}
    logger_helper.call(os.getenv('LOGGER_URL',
                                 'http://127.0.0.1:5001/api/v1/skipper/logger/log_workflow'),
                       params)

    return queue_name
