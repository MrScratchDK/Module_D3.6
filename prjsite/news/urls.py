from django.urls import path
from .views import main, default

urlpatterns = [
    path('news/', main, name='main'),
    path('new/<str:slug>', default, name='default'),
]