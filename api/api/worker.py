from celery import Celery
import os


app = Celery(
    'skipper_celery_api',
    broker=os.getenv('RABBITMQ_BROKER', 'pyamqp://skipper:welcome1@127.0.0.1//'),
    backend='rpc://',
    include=['api.tasks']
)
