from django.urls import include, path
from django.contrib import admin
from . import views

urlpatterns = [
    path("login/", views.login, name='login'),
    path('<int:key_id>/', views.id, name = 'id')
]