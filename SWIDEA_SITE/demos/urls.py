from django.urls import path
from .views import *

app_name="demos"

urlpatterns = [

    path('', main, name='main'), 
    path('<int:pk>/', ideaDetail, name='ideaDetail'),
    path('update/<int:pk>/', ideaUpdate, name='ideaUpdate'),
    path('delete/<int:pk>', ideaDelete, name='ideaDelete'),
    path('devToolRegister/', devToolRegister, name='devToolRegister'),
    path('devToolList/', devToolList, name='devToolList' ),
    path('devToolDetail/<int:pk>/', devToolDetail, name='devToolDetail' ),
    path('devTooldelete/<int:pk>', devDelete, name='devDelete'),
    path('devToolUpdate/<int:pk>', devToolUpdate, name='devToolUpdate'),

]