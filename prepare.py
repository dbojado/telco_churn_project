import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.impute import SimpleImputer

from acquire import get_telco_data

def telco_data_prep():
    df = get_telco_data()
    return df