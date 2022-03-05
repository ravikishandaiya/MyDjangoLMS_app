## manual

from django.urls import path
from . import views

from django.urls import re_path

urlpatterns = [
    path('',views.index, name='index'),
    path('index',views.index, name='index'),
    path('books',views.books, name='books'),
    path('books/',views.books, name='books'),
    path('subscribers',views.subscribers, name='subscribers'),
    path('subscribers/',views.subscribers, name='subscribers'),
    re_path(r'^books/(?P<id>.+)$', views.books_by_id), 
    re_path(r'^subscribers/(?P<ids>.+)$',views.subscribers_by_id, name="subscribers_by_id"),
    path('users',views.distinct_subscribers, name='distinct'),
    path('users/',views.distinct_subscribers, name='distinct'),
]
