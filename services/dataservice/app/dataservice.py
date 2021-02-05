from concurrent import futures
from io import BytesIO
import numpy as np

import grpc
import dataservice_pb2_grpc

from dataservice_pb2 import BostonHousingResponse

import datahelper as dh

class BostonHousingService(dataservice_pb2_grpc.BostonHousingServicer):
    def PrepareData(self, request, context):

        norm_train_X, norm_test_X, norm_val_X, train_Y, test_Y, val_Y = dh.prepare_datasets(request.test_size)
        print()
        print('Normalized training X:', norm_train_X.shape)
        print('Normalized testing X:', norm_test_X.shape)
        print('Normalized validation X:', norm_val_X.shape)
        print('Training Y:', train_Y[0].shape)
        print('Testing Y:', test_Y[0].shape)
        print('Validation Y:', val_Y[0].shape)

        norm_train_X_bytes = BytesIO()
        np.save(norm_train_X_bytes, norm_train_X, allow_pickle=False)
        norm_test_X_bytes = BytesIO()
        np.save(norm_test_X_bytes, norm_test_X, allow_pickle=False)
        norm_val_X_bytes = BytesIO()
        np.save(norm_val_X_bytes, norm_val_X, allow_pickle=False)
        train_Y_bytes = BytesIO()
        np.save(train_Y_bytes, train_Y, allow_pickle=False)
        test_Y_bytes = BytesIO()
        np.save(test_Y_bytes, test_Y, allow_pickle=False)
        val_Y_bytes = BytesIO()
        np.save(val_Y_bytes, val_Y, allow_pickle=False)

        return BostonHousingResponse(norm_train_x=norm_train_X_bytes.getvalue(), norm_test_x=norm_test_X_bytes.getvalue(),
                                     norm_val_x=norm_val_X_bytes.getvalue(), train_y=train_Y_bytes.getvalue(),
                                     test_y=test_Y_bytes.getvalue(), val_y=val_Y_bytes.getvalue())

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    dataservice_pb2_grpc.add_BostonHousingServicer_to_server(
        BostonHousingService(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()