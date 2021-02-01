from fastapi import APIRouter
import dataservice.app.api.dataprocessor as processor

dataservice = APIRouter()

@dataservice.get('/')
def test():
    return 'API is running'

@dataservice.post('/execute')
def prepare_data():

    processor.prepare_datasets()

    return 'OK'