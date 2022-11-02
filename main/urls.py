from django.urls import path
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='links'),
    path('api/status', views.CheckStatusView.as_view())
]