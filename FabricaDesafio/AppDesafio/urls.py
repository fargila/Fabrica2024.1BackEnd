from django.urls import path
from AppDesafio.API import views

urlpatterns = [
    path('db/', views.alocarDadosAPI, name='pegar_dados')
]
