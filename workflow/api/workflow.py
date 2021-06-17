import json


def get_queue_name(service_id):
    f = open('./api/workflow.json')
    data = json.load(f)

    queue_name = '-'
    for x in data:
        for key, value in x.items():
            if key == service_id:
                queue_name = value

    f.close()

    return queue_name
