
from apps.gateway import views
from django.urls import path

urlpatterns = [
    path('', views.GatewayView.as_view(), name='gateway')
]
