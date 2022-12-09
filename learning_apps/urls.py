"""Defines url patterns for learning_apps."""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home page.
    path('', views.index, name='index'),
    #show all Topics.
    path('topic/', views.topics, name='topics'),
    # Detail page for a single topic.
    path('topics/<int:topic_id>/', views.topic, name='topic'),
]