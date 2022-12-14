from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='monografia_index'),
    path('adicionar/', views.adicionar, name='monografia_adicionar'),
    path('editar/<int:id>/', views.editar, name='monografia_editar'),
    path('apagar/<int:id>/', views.apagar, name='monografia_apagar'),
    path('pesquisar/', views.monografia_filter_list, name='monografia_pesquisar'),
]