"""Defines URL patterns for learning_apps."""

from django.urls import path

from . import views

#from django.conf.urls import url

app_name = 'learning_apps'
urlpatterns = [
    # Home page.
    path('', views.index, name='index'),
    #url(r'^topics/$', views.topics, name='topics'),  #(not working in old version.)
     # Show all topics.
    path('topics/', views.topics, name='topics'),
     # Detail page for a single topic.
    path('topics/<int:topic_id>/', views.topic, name='topic'),
]
