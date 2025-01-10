from django.urls import path
from .views import *

app_name="movie"

urlpatterns = [

    path('', index, name='index'),
    path('', review, name='review'),
    path('<int:pk>/', detail, name='detail'),
    path('update/<int:pk>/', update, name='update'),
    path('delete/<int:pk>', delete, name='delete')
]