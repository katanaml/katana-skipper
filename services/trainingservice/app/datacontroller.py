from io import BytesIO
import numpy as np

from dataservice_pb2 import ParamsRequest

class DataController():
    def __init__(self, client):
        self.client = client

    def fetch_data(self, test_size):
        request = ParamsRequest(test_size=test_size)
        response = self.client.PrepareData(request)

        norm_train_X_bytes = BytesIO(response.norm_train_x)
        norm_train_X = np.load(norm_train_X_bytes, allow_pickle=False)
        norm_test_X_bytes = BytesIO(response.norm_test_x)
        norm_test_X = np.load(norm_test_X_bytes, allow_pickle=False)
        norm_val_X_bytes = BytesIO(response.norm_val_x)
        norm_val_X = np.load(norm_val_X_bytes, allow_pickle=False)
        train_Y_bytes = BytesIO(response.train_y)
        train_Y = np.load(train_Y_bytes, allow_pickle=False)
        test_Y_bytes = BytesIO(response.test_y)
        test_Y = np.load(test_Y_bytes, allow_pickle=False)
        val_Y_bytes = BytesIO(response.val_y)
        val_Y = np.load(val_Y_bytes, allow_pickle=False)

        train_Y_1 = train_Y[0]
        train_Y_2 = train_Y[1]
        train_Y = (train_Y_1, train_Y_2)

        test_Y_1 = test_Y[0]
        test_Y_2 = test_Y[1]
        test_Y = (test_Y_1, test_Y_2)

        val_Y_1 = val_Y[0]
        val_Y_2 = val_Y[1]
        val_Y = (val_Y_1, val_Y_2)

        return norm_train_X, norm_test_X, norm_val_X, train_Y, test_Y, val_Y

