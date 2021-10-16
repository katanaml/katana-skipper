import os
import json
import base64
import shutil


class StorageService(object):
    def __init__(self):
        pass

    def call(self, data):
        data_json = json.loads(data)

        model_name = data_json['name']
        archive_name = data_json['archive_name']
        stats_name = data_json['stats_name']
        model_decoded = base64.b64decode(data_json['model'])
        stats_decoded = base64.b64decode(data_json['stats'])

        try:
            with open(os.getenv('MODELS_FOLDER', '../../models/serving/') + archive_name, 'wb') as model_file_decoded:
                model_file_decoded.write(model_decoded)

            shutil.unpack_archive(os.getenv('MODELS_FOLDER', '../../models/serving/') + archive_name,
                                  os.getenv('MODELS_FOLDER', '../../models/serving/') + model_name,
                                  format='zip')

            with open(os.getenv('MODELS_FOLDER', '../../models/serving/') + stats_name, 'wb') as stats_file_decoded:
                stats_file_decoded.write(stats_decoded)
        except:
            print('Model file saving ignored, sharing same node')

        return 'OK', 'storage'
