import os
import pandas as pd
import numpy as np
import env

def get_connection(db, username=env.username, host=env.host, password=env.password):
    return f'mysql+pymysql://{username}:{password}@{host}/{db}'

    
def get_telecom_data():
    file = 'telecom_data.csv'

    if os.path.isfile(file):
        return pd.read_csv('telecom_data.csv')
    else:
        df = pd.read_sql("""
                        select *
                        from customers
                        join internet_service_types using(internet_service_type_id)
                        join contract_types using(contract_type_id)
                        join payment_types using(payment_type_id);
                        """,
                        get_connection('telco_churn')
                        )
        
        df.to_csv('telecom_data.csv', index=False)
        return df