from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def show_meta_table(request):
    return render(request, 'meta.html')