from django.urls import path
from . import views

#URL

urlpatterns = [
    path('hello/', views.say_hello)
]