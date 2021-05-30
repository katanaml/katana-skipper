import os
import json
import tensorflow as tf
import pandas as pd


class ServingService(object):
    def __init__(self):
        pass

    def call(self, data):
        data_json = json.loads(data)
        payload = pd.DataFrame(data_json['data'], index=['i', ])
        print(payload)

        models = self.get_immediate_subdirectories('../models/')
        saved_model = tf.keras.models.load_model('../models/' + max(models))

        result = [0]
        response = json.dumps(result)

        return response, data_json['task_type']

    def get_immediate_subdirectories(self, a_dir):
        return [name for name in os.listdir(a_dir)
                if os.path.isdir(os.path.join(a_dir, name))]
