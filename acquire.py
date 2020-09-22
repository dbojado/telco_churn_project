import pandas as pd 
import os
from env

def get_connection(db, username=env.username, host=env.host, password=env.password):
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