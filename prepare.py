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
def train_test_validate(telco_data_df):
    from sklearn.model_selection import train_test_split

    train_validate, test = train_test_split(telco_data_df, test_size = .10, random_state = 123)

    train, validate = train_test_split(train_validate, test_size = .20, random_state = 123)

    print("train shape: ", train.shape, ", validate shape: ", validate.shape, ", test shape: ", test.shape)

    total = telco_data_df.count()[0]
    print("\ntrain percent: ", round(((train.shape[0])/total),2) * 100, 
            ", validate percent: ", round(((validate.shape[0])/total),2) * 100, 
            ", test percent: ", round(((test.shape[0])/total),2) * 100)

    return train, validate, test