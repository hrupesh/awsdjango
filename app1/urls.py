
from django.urls import path, include
from .views import hello

urlpatterns = [
    path('', hello, name='hello'),
]
