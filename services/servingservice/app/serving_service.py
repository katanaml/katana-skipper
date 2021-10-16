import os
import json
import tensorflow as tf
import pandas as pd
import numpy as np


class ServingService(object):
    def __init__(self):
        pass

    def call(self, data):
        data_json = json.loads(data)
        payload = pd.DataFrame(data_json['data'], index=[0, ])
        payload.columns = [x.upper() for x in payload.columns]

        response = '{}'

        try:
            train_stats = pd.read_csv(os.getenv('MODELS_FOLDER', '../models/serving/') + 'train_stats.csv', index_col=0)
            x = np.array(self.norm(payload, train_stats))

            models = self.get_immediate_subdirectories(os.getenv('MODELS_FOLDER', '../models/serving/'))
            saved_model = tf.keras.models.load_model(os.getenv('MODELS_FOLDER', '../models/serving/') + max(models))

            predictions = saved_model.predict(x)

            result = {
                'price': str(predictions[0][0][0]),
                'ptratio': str(predictions[1][0][0])
            }
            response = json.dumps(result)
        except:
            print('Model is not ready for serving')

        return response, data_json['task_type']

    def get_immediate_subdirectories(self, a_dir):
        return [name for name in os.listdir(a_dir)
                if os.path.isdir(os.path.join(a_dir, name))]

    def norm(self, x, train_stats):
        return (x - train_stats['mean']) / train_stats['std']
