from django.urls import path
from . import views

app_name = 'customer'

urlpatterns = [
    path('', views.index, name='customer'),
    path('login/', views.CustomerLogin.as_view(), name='login'),
    path('register/', views.CustomerRegister.as_view(), name='register'),
    path('logout/', views.CustomerLogout.as_view(), name='logout'),
    path('password_lost/', views.CustomerPasswordLost.as_view(), name='password_lost'),
    path('info/', views.CustomerInfo.as_view(), name='info'),
]
