from django.urls import path
from .views import register, login_view, dashboard

urlpatterns = [
    path('', register, name='register'),
    path('login/', login_view, name='login'),
    path('dashboard/', dashboard, name='dashboard'),
]
