from django.urls import path
from exercise import views

urlpatterns = [
    path('hello', views.hello_world, name='hello'),
]
