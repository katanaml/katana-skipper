import json
import requests


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
    requests.post('http://127.0.0.1:5001/api/v1/skipper/logger/log_workflow', json=params)

    return queue_name
