
from django.urls import path,include
from . import views

urlpatterns = [
    path('photos/', views.index, name='index'),
]
