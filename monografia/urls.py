from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='monografia_index'),
    path('adicionar/', views.adicionar,name='adicionar'),
    path('pesquisar/', views.monografia_filter_list,name='pesquisar')
]