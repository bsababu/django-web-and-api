from django.urls import path
from .views import dashboard, ChartData
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('api/chart/', ChartData.as_view(), name='chart-data'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
]
