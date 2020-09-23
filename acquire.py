#Library imports
import pandas as pd 
import os
from env import host, username, password 

#Connect to database
def get_connection(db, username=username, host=host, password=password):
    return f'mysql+pymysql://{username}:{password}@{host}/{db}'

#Get csv data file
def get_telco_data():
    file = 'telco_data_1.csv'

    if os.path.isfile(file):
        return pd.read_csv('telco_data_1.csv')
    else:
        df = pd.read_sql("""
                        SELECT *
                        JOIN internet_service_types using(internet_service_type_id)
                        JOIN contract_types using(contract_type_id)
                        JOIN payment_types using(payment_type_id);
                        """,
                        get_connection('telco_churn')
                        )
        
        df.to_csv('telco_data_1.csv', index=False)
        return df