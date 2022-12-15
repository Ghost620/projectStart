from django.shortcuts import render
import json
from .WorldBank import fetchWorldBankDB

def index(request):
    return render(request, 'index.html')

def show_meta_table(request):
    if request.method == 'POST':
        df = fetchWorldBankDB()
        json_records = df.reset_index().to_json(orient ='records')
        data = []
        data = json.loads(json_records)
        context = {'data': data, 'columns': list(data[0].keys())[1:] }
    
        return render(request, 'meta.html', context)