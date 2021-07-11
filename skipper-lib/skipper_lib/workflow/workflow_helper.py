import requests


def call(task_type, url, mode):
    valid = {'_sync', '_async'}
    if mode not in valid:
        raise ValueError("call: status must be one of %r." % valid)

    r = requests.get(url + task_type + mode)
    queue_name = r.json()['queue_name']
    return queue_name
