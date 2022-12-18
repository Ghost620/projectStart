from sqlalchemy import create_engine
from dotenv import load_dotenv
import os, json
import pandas as pd

load_dotenv()
database=os.getenv('LOCAL_DB_NAME')
user=os.getenv('LOCAL_DB_USER')
password=os.getenv('LOCAL_DB_PASSWORD')
port=int(os.getenv('DB_PORT'))
host=os.getenv('DB_HOST')

def dict2htmltable(data):
    html = '<thead class="sticky top-0 text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">' + '<tr>' + '<th colspan="7" class="heads py-3 px-6 font-medium text-white text-center"> </th>' + '</tr>' + '<tr>' + ''.join('<th scope="col" class="py-3 px-6 text-center">' + x + '</th>' for x in data[0].keys()) + '</tr>' + '<tbody>'
    
    for d in data:
        html += '<tr class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600">' + ''.join('<td class="py-4 px-6 font-medium text-white text-center">' + f'{x}' + '</td>' for x in d.values()) + '</tr>'
    return '<table class="w-full text-sm text-left text-gray-500 dark:text-gray-400">' + html + '</tbody>' + '</table>'

engine = create_engine(f'postgresql://{user}:{password}@{host}/{database}')

def fetchWorldBankDB():
    global engine

    all_tables_query = '''
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema='public'
        AND table_type='BASE TABLE';
    '''

    df = pd.read_sql_query(all_tables_query, engine)
    world_bank_tables = [i for i in df['table_name'] if 'world_bank' in i]
    queries = [f'''SELECT * FROM {table};''' for table in world_bank_tables]
    all_tables = [pd.read_sql_query(quer, engine, index_col='id') for quer in queries]
    data = [json.loads(df.reset_index().to_json(orient ='records')) for df in all_tables]
    tables = [dict2htmltable(df) for df in data]
    table_names = [name.replace('world_bank_', '').replace('_', ' ') for name in world_bank_tables]

    return tables, table_names