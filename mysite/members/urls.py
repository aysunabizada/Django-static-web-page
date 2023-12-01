
from . import views
from django.urls import path
app_name = "members"
urlpatterns = [
    path('test', views.members, name='members'),
]
