from django.shortcuts import render
from django import forms

def index(request):
    return render(request, 'index.html')

def show_meta_table(request):
    if request.method == 'POST':
        print(request.POST['data_source'])

    return render(request, 'meta.html', {'table_name': request.POST['data_source']})