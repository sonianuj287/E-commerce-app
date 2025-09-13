from django.urls import path 
from .views import createAPI

urlpatterns=[
    path('users/',createAPI.as_view())
]