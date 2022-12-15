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
        context = {'data': data}
    
        return render(request, 'meta.html', context)
        #return render(request, 'meta.html', {'table_name': request.POST['data_source'], 'context': context})