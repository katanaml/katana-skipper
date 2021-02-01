# Importing the libraries
import pandas as pd

# Importing the Boston Housing dataset
from sklearn.datasets import load_boston

def prepare_datasets():
    # Loading the Boston Housing dataset
    boston = load_boston()

    # Initializing the dataframe
    data = pd.DataFrame(boston.data)

    return 'OK'