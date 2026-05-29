from django.urls import path
from . import views

urlpatterns = [
    path('', views.extra_inicio, name='extra_inicio'),
]
