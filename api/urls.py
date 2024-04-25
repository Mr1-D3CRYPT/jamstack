from django.urls import path
from . import views
from rest_framework import routers
from .api import ComplaintViewSet

router = routers.DefaultRouter()
router.register('api',ComplaintViewSet,'Complaint')

urlpatterns = [
    path('',views.profile),
    path('profile',views.profile),
    path('login',views.login_view),
    path('register',views.register),
    path('logout',views.logout_view),
    path('submit_complaint',views.submit_complaint),
    path('delete_complaint',views.delete_complaint),
]+router.urls
