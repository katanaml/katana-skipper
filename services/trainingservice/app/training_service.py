class TrainingService(object):
    def __init__(self):
        pass

    def call(self, data):
        self.run_training(data['payload'])

        return 'TASK_COMPLETED'

    def run_training(self, dataset_split):
        norm_train_x, norm_test_x, norm_val_x, train_y, test_y, val_y = self.prepare_datasets(dataset_split)

    def prepare_datasets(self, dataset_split):
        pass