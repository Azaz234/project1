from django.contrib import admin
from django.urls import path
from .import views
from .import billing_api

urlpatterns = [
    path('ajaj',views.index),
    path('azaz/',billing_api.employeeAPI.as_view()),
    path('azaz/<int:pk>/',billing_api.employeeAPI.as_view()),
]