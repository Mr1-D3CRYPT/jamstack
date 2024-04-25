from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('profile',views.profile),
    path('login',views.login_view),
    path('register',views.register),
    path('logout',views.logout_view),
    path('submit_complaint',views.submit_complaint),
    path('delete_complaint',views.delete_complaint),
]