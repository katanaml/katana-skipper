import grpc

import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, Input

from dataservice_pb2_grpc import BostonHousingStub

import datacontroller as dc


def build_model(columns_len):
    # Define model layers.
    input_layer = Input(shape=(columns_len,))
    first_dense = Dense(units='128', activation='relu')(input_layer)
    # Y1 output will be fed from the first dense
    y1_output = Dense(units='1', name='price_output')(first_dense)

    second_dense = Dense(units='128', activation='relu')(first_dense)
    # Y2 output will be fed from the second dense
    y2_output = Dense(units='1', name='ptratio_output')(second_dense)

    # Define the model with the input layer and a list of output layers
    model = Model(inputs=input_layer, outputs=[y1_output, y2_output])

    return model


class TrainingService():
    def __init__(self):
        channel = grpc.insecure_channel("localhost:50051")
        self.client = BostonHousingStub(channel)

    def fetch_data(self):
        data_controller = dc.DataController(self.client)
        return data_controller.fetch_data(0.2)

    def run_training(self):
        norm_train_X, norm_test_X, norm_val_X, train_Y, test_Y, val_Y = self.fetch_data()

        model = build_model(len(norm_train_X[0]))

        # Specify the optimizer, and compile the model with loss functions for both outputs
        optimizer = tf.keras.optimizers.SGD(lr=0.001)
        model.compile(optimizer=optimizer,
                      loss={'price_output': 'mse', 'ptratio_output': 'mse'},
                      metrics={'price_output': tf.keras.metrics.RootMeanSquaredError(),
                               'ptratio_output': tf.keras.metrics.RootMeanSquaredError()})

        # Train the model for 100 epochs
        history = model.fit(norm_train_X, train_Y,
                            epochs=100, batch_size=10, validation_data=(norm_test_X, test_Y))

        # Test the model and print loss and rmse for both outputs
        loss, Y1_loss, Y2_loss, Y1_rmse, Y2_rmse = model.evaluate(x=norm_val_X, y=val_Y)

        print()
        print(f'loss: {loss}')
        print(f'price_loss: {Y1_loss}')
        print(f'ptratio_loss: {Y2_loss}')
        print(f'price_rmse: {Y1_rmse}')
        print(f'ptratio_rmse: {Y2_rmse}')