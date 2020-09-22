import pandas as pd 
import os
from env import host, username, password

def get_connection(db, username=username, host=host, password=password):
    return f'mysql+pymysql://{username}:{password}@{host}/{db}'

def get_telco_data():
    file = 'telco_data.csv'

    if os.path.isfile(file):
        return pd.read_csv('telco_data.csv')
    else:
        df = pd.read_sql("""
                        SELECT *
                        FROM customers;
                        """,
                        get_connection('telco_churn')
                        )
        
        df.to_csv('telco_data.csv', index=False)
        return df