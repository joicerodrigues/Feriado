from django.urls import path
from . import views
urlpatterns = [
    path('', views.verifica_feriado),
]