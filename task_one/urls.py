
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^task-one/', views.task_one, name='task_one'),
]
