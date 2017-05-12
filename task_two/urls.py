from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^task-two/', views.task_two, name='task_two'),
]
