from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()
database=os.getenv('LOCAL_DB_NAME')
user=os.getenv('LOCAL_DB_USER')
password=os.getenv('LOCAL_DB_PASSWORD')
port=int(os.getenv('DB_PORT'))
host=os.getenv('DB_HOST')
engine = create_engine(f'postgresql://{user}:{password}@{host}/{database}')

def fetchWorldBankDB():
    global engine
    query = '''SELECT * FROM world_bank_databases;'''
    df = pd.read_sql_query(query, engine)
    return df