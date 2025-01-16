from django.urls import path
from .views import *

app_name="create"

urlpatterns = [

    path('register/', register, name='register'), 
    path('toggle_star/<int:post_id>/', toggle_star, name='toggle_star'),
    path('update-interest/<int:post_id>/', update_interest, name='update_interest'),
]