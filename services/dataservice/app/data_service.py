import os

import pandas as pd
import numpy as np
import json

# Importing the Boston Housing dataset
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split


class DataService(object):
    def __init__(self):
        pass

    def call(self, data):
        data_json = json.loads(data)
        norm_train_x, norm_test_x, norm_val_x, train_y, test_y, val_y = self.prepare_datasets(float(data_json['payload']))

        print()
        print('Normalized training X:', norm_train_x.shape)
        print('Normalized testing X:', norm_test_x.shape)
        print('Normalized validation X:', norm_val_x.shape)
        print('Training Y:', train_y[0].shape)
        print('Testing Y:', test_y[0].shape)
        print('Validation Y:', val_y[0].shape)
        print()

        train_y_list = list(train_y)
        train_y_list[0] = train_y_list[0].tolist()
        train_y_list[1] = train_y_list[1].tolist()
        train_y = tuple(train_y_list)

        test_y_list = list(test_y)
        test_y_list[0] = test_y_list[0].tolist()
        test_y_list[1] = test_y_list[1].tolist()
        test_y = tuple(test_y_list)

        val_y_list = list(val_y)
        val_y_list[0] = val_y_list[0].tolist()
        val_y_list[1] = val_y_list[1].tolist()
        val_y = tuple(val_y_list)

        data = [norm_train_x.tolist(),
                norm_test_x.tolist(),
                norm_val_x.tolist(),
                train_y,
                test_y,
                val_y]

        response = json.dumps(data)

        return response, data_json['task_type']

    def prepare_datasets(self, data_split):
        # Loading the Boston Housing dataset
        boston = load_boston()

        # Initializing the dataframe
        data = pd.DataFrame(boston.data)

        # Adding the feature names to the dataframe
        data.columns = boston.feature_names

        # Adding target variable to dataframe
        data['PRICE'] = boston.target

        # Split the data into train and test with 80 train / 20 test
        train, test = train_test_split(data, test_size=data_split, random_state=1)
        train, val = train_test_split(train, test_size=data_split, random_state=1)

        train_y = self.format_output(train)
        test_y = self.format_output(test)
        val_y = self.format_output(val)

        # Normalize the training and test data
        norm_train_x = np.array(self.norm(train, train))
        norm_test_x = np.array(self.norm(test, train))
        norm_val_x = np.array(self.norm(val, train))

        return norm_train_x, norm_test_x, norm_val_x, train_y, test_y, val_y

    # Helper functions
    def norm(self, x, train):
        # Get PRICE and PTRATIO as the 2 outputs and format them as np arrays
        # PTRATIO - pupil-teacher ratio by town
        train_stats = train.describe()
        train_stats = train_stats.transpose()

        train_stats.to_csv(os.getenv('STATS_FILE', '../models/train_stats.csv'),
                           header=True)

        return (x - train_stats['mean']) / train_stats['std']

    def format_output(self, data):
        y1 = data.pop('PRICE')
        y1 = np.array(y1)
        y2 = data.pop('PTRATIO')
        y2 = np.array(y2)
        return y1, y2
