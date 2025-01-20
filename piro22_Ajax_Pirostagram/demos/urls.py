from django.urls import path
from . import views

app_name = 'demos'

urlpatterns = [
    path('', views.main, name='main'),
    path('create/', views.create, name='create'),
    path('post/<int:pk>', views.post, name='post'),
    path('like_ajax/', views.like_ajax, name='like_ajax'),
    path('comment_ajax/', views.comment_ajax, name='comment_ajax'),
    path('delete_comment_ajax/', views.delete_comment_ajax, name='delete_comment_ajax'),
]
