from django.contrib import admin
from django.urls import path
from .views import index, show_meta_table

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('meta/', show_meta_table, name='show_meta_table')
]
