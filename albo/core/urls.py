from django.urls import path
from . import views

urlpatterns = [
    path('',views.public,name='public'),
    path('login/',views.login,name='login'),
    path('albo/',views.albo,name="main"),
]