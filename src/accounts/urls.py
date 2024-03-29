from django.urls import path
from .views import register_view, login_view, logout_view, dashboard_view

app_name = 'accounts'

urlpatterns = [
    path('dashboard', dashboard_view, name='dashboard'),
    path('signup', register_view, name='register'),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
]
