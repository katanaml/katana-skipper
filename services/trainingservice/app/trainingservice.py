import grpc

from app.dataservice_pb2_grpc import BostonHousingStub

import app.datacontroller as dc

class TrainingService():
    def __init__(self):
        channel = grpc.insecure_channel("localhost:50051")
        self.client = BostonHousingStub(channel)

    def fetch_data(self):
        data_controller = dc.DataController(self.client)
        return data_controller.fetch_data(0.2)

    def run_training(self):
        norm_train_X, norm_test_X, norm_val_X, train_Y, test_Y, val_Y = self.fetch_data()
        print('Normalized training X:', norm_train_X.shape)
        print('TRAINING')