from django.shortcuts import render
from .WorldBank import fetchWorldBankDB

def index(request):
    return render(request, 'index.html')

def show_meta_table(request):
    if request.method == 'POST':
        if ( request.POST['data_source'] and request.POST['view_mode'] and request.POST['activity']):

            if ( request.POST['activity'] == 'VALL' and request.POST['view_mode'] == 'VALMT' ):
                all_tables, table_names = fetchWorldBankDB()
                context = { 'table_name': request.POST['data_source'], 'data': all_tables, 'table_names': table_names }
                return render(request, 'meta.html', context)
