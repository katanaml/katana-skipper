from celery import Celery
import os


app = Celery(
    'skipper_celery_api',
    broker=os.getenv('RABBITMQ_BROKER'),
    backend='rpc://',
    include=['api.tasks']
)
