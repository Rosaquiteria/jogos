from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:jogo_id>', views.jogo, name='jogo'),
    path('buscar', views.buscar, name= 'buscar'),
    path('criar/jogo', views.criar_jogo, name='criar_jogo')
]
