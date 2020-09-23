#Library imports
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.impute import SimpleImputer

from acquire import get_telco_data

#Function for data prep
def telco_data_prep():
    df = get_telco_data()
    df.total_charges = df.total_charges.str.strip()
    df.total_charges = df.total_charges.replace('', 0) 
    df.total_charges = df.total_charges.astype("float") 
    df.churn.replace(['Yes', 'No'], [1,0], inplace = True)
    return df


#Function for spliting data (train, test, validate)
def train_test_validate():

    train_validate, test = train_test_split(df, test_size = .2, random_state = 123)
    train, validate = train_test_split(train_validate, test_size = .3, random_state = 123)

    return train, validate, test