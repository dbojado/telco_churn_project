import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.impute import SimpleImputer

from acquire import get_telecom_data

def telcom_data_prep():
    df = get_telecom_data()
    return df