from django.urls import path
from .views import *

app_name="create"

urlpatterns = [

    path('', create, name='create'), 

]