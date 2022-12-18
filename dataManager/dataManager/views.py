from django.shortcuts import render
import json
from .WorldBank import fetchWorldBankDB

def index(request):
    return render(request, 'index.html')

def show_meta_table(request):
    if request.method == 'POST':

        all_tables = fetchWorldBankDB()
        data = [json.loads(df.reset_index().to_json(orient ='records')) for df in all_tables]

        context = {'table_name': request.POST['data_source'], 'data': data }
    
        return render(request, 'meta.html', context)
