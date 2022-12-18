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

all_tables_query = '''
    SELECT table_name
    FROM information_schema.tables
    WHERE table_schema='public'
    AND table_type='BASE TABLE';
'''

df = pd.read_sql_query(all_tables_query, engine)

def fetchWorldBankDB():
    global engine, df
    world_bank_tables = [i for i in df['table_name'] if 'world_bank' in i]
    queries = [f'''SELECT * FROM {table};''' for table in world_bank_tables]
    all_dbs = [pd.read_sql_query(quer, engine) for quer in queries]
    return all_dbs