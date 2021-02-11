from io import BytesIO
import numpy as np

from app.dataservice_pb2 import ParamsRequest

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

        return norm_train_X, norm_test_X, norm_val_X, train_Y, test_Y, val_Y

