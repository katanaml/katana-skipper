import grpc

from dataservice_pb2_grpc import BostonHousingStub
from dataservice_pb2 import ParamsRequest

from io import BytesIO
import numpy as np

channel = grpc.insecure_channel("localhost:50051")
client = BostonHousingStub(channel)

request = ParamsRequest(test_size=0.2)

response = client.PrepareData(request)
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

print('Normalized training X:', norm_train_X.shape)
print('Normalized testing X:', norm_test_X.shape)
print('Normalized validation X:', norm_val_X.shape)
print('Training Y:', train_Y[0].shape)
print('Testing Y:', test_Y[0].shape)
print('Validation Y:', val_Y[0].shape)

