from fastapi import APIRouter
import dataservice.app.api.dataprocessor as processor

dataservice = APIRouter()

@dataservice.get('/')
def test():
    return 'API is running'

@dataservice.post('/execute')
def prepare_data():

    norm_train_X, norm_test_X, norm_val_X, train_Y, test_Y, val_Y = processor.prepare_datasets()

    return True