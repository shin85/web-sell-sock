from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('<int:plan_id>/', views.OrderChoise.as_view(), name='order'),
]
