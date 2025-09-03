from .views import main, detail
from django.urls import path

urlpatterns = [
    path('', main, name='main'),
    path('sam/', detail, name='detail'),
]