import requests


def call(logger, params):
    try:
        requests.post(logger, json=params)
    except requests.exceptions.RequestException as e:
        print('Logger service is not available')
