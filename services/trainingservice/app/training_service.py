import numpy as np
import json
import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, Input
from skipper_lib.events.event_producer import EventProducer
from skipper_lib.events.exchange_producer import ExchangeProducer
import calendar
import time
import shutil
import base64
import os


class TrainingService(object):
    def __init__(self):
        pass

    def call(self, data):
        data_json = json.loads(data)

        self.run_training(data)

        payload = {
            'result': 'TASK_COMPLETED'
        }
        response = json.dumps(payload)

        return response, data_json['task_type']

    def build_model(self, columns_len):
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

    def prepare_datasets(self, data, event_producer):
        response = event_producer.call(os.getenv('QUEUE_NAME_DATA', 'skipper_data'), data)

        data = json.loads(response)
        norm_train_x = np.array(data[0])
        norm_test_x = np.array(data[1])
        norm_val_x = np.array(data[2])

        train_y = data[3]
        train_y_list = list(train_y)
        train_y_list[0] = np.array(train_y[0])
        train_y_list[1] = np.array(train_y[1])
        train_y = tuple(train_y_list)

        test_y = data[4]
        test_y_list = list(test_y)
        test_y_list[0] = np.array(test_y[0])
        test_y_list[1] = np.array(test_y[1])
        test_y = tuple(test_y_list)

        val_y = data[5]
        val_y_list = list(val_y)
        val_y_list[0] = np.array(val_y[0])
        val_y_list[1] = np.array(val_y[1])
        val_y = tuple(val_y_list)

        print()
        print('Normalized training X:', norm_train_x.shape)
        print('Normalized testing X:', norm_test_x.shape)
        print('Normalized validation X:', norm_val_x.shape)
        print('Training Y:', train_y[0].shape)
        print('Testing Y:', test_y[0].shape)
        print('Validation Y:', val_y[0].shape)
        print()

        return norm_train_x, norm_test_x, norm_val_x, train_y, test_y, val_y

    def run_training(self, data):
        event_producer = EventProducer(username=os.getenv('RABBITMQ_USER', 'skipper'),
                                       password=os.getenv('RABBITMQ_PASSWORD', 'welcome1'),
                                       host=os.getenv('RABBITMQ_HOST', '127.0.0.1'),
                                       port=os.getenv('RABBITMQ_PORT', 5672),
                                       service_name=os.getenv('SERVICE_NAME', 'training'),
                                       logger=os.getenv('LOGGER_PRODUCER_URL',
                                                        'http://127.0.0.1:5001/api/v1/skipper/logger/log_producer'))

        norm_train_x, norm_test_x, norm_val_x, train_y, test_y, val_y = self.prepare_datasets(data, event_producer)

        model = self.build_model(len(norm_train_x[0]))

        # Specify the optimizer, and compile the model with loss functions for both outputs
        optimizer = tf.keras.optimizers.SGD(learning_rate=0.001)
        model.compile(optimizer=optimizer,
                      loss={'price_output': 'mse', 'ptratio_output': 'mse'},
                      metrics={'price_output': tf.keras.metrics.RootMeanSquaredError(),
                               'ptratio_output': tf.keras.metrics.RootMeanSquaredError()})

        # Train the model for 100 epochs
        history = model.fit(norm_train_x, train_y,
                            epochs=50,
                            batch_size=10,
                            validation_data=(norm_test_x, test_y),
                            verbose=0)

        # Test the model and print loss and rmse for both outputs
        loss, Y1_loss, Y2_loss, Y1_rmse, Y2_rmse = model.evaluate(x=norm_val_x, y=val_y)

        print()
        print(f'loss: {loss}')
        print(f'price_loss: {Y1_loss}')
        print(f'ptratio_loss: {Y2_loss}')
        print(f'price_rmse: {Y1_rmse}')
        print(f'ptratio_rmse: {Y2_rmse}')
        print()

        # Save model
        ts = calendar.timegm(time.gmtime())
        model.save(os.getenv('MODELS_FOLDER', '../models/model_boston_') + str(ts) + '/', save_format='tf')

        # Send model to the queue
        shutil.make_archive(base_name=os.getenv('MODELS_FOLDER', '../models/model_boston_') + str(ts),
                            format='zip',
                            root_dir=os.getenv('MODELS_FOLDER', '../models/model_boston_') + str(ts))

        model_encoded = None
        try:
            with open(os.getenv('MODELS_FOLDER', '../models/model_boston_') + str(ts) + '.zip', 'rb') as model_file:
                model_encoded = base64.b64encode(model_file.read())
        except Exception as e:
            print(str(e))

        stats_encoded = None
        try:
            with open(os.getenv('STATS_FILE', '../models/train_stats.csv'), 'rb') as stats_file:
                stats_encoded = base64.b64encode(stats_file.read())
        except Exception as e:
            print(str(e))

        model_encoded = model_encoded.decode('utf-8')
        stats_encoded = stats_encoded.decode('utf-8')

        data = {
            'name': 'model_boston_' + str(ts),
            'archive_name': 'model_boston_' + str(ts) + '.zip',
            'model': model_encoded,
            'stats': stats_encoded,
            'stats_name': 'train_stats.csv'
        }
        content = json.dumps(data)

        exchange_producer = ExchangeProducer(username=os.getenv('RABBITMQ_USER', 'skipper'),
                                             password=os.getenv('RABBITMQ_PASSWORD', 'welcome1'),
                                             host=os.getenv('RABBITMQ_HOST', '127.0.0.1'),
                                             port=os.getenv('RABBITMQ_PORT', 5672),
                                             service_name=os.getenv('SERVICE_NAME', 'training'),
                                             logger=os.getenv('LOGGER_PRODUCER_URL',
                                                              'http://127.0.0.1:5001/api/v1/skipper/logger/log_producer'))

        exchange_producer.call(exchange=os.getenv('QUEUE_NAME_STORAGE', 'skipper_storage'),
                               exchange_type='fanout',
                               payload=content)
