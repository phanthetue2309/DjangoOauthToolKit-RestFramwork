from django.urls import path

from .api import views

urlpatterns = [
    path('register/', views.register),
    path('login/', views.login),
    path('token/refresh/', views.refresh_token),
    path('token/revoke/', views.revoke_token),
]
