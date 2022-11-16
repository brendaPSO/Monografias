from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='core_index'),
    path('adicionar/', views.adicionar, name='core_adicionar'),
    path('editar/<int:id>/', views.editar, name='core_editar'),
    path('apagar/<int:id>/', views.apagar, name='core_apagar'),
]