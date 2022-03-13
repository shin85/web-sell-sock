from django.urls import path
from . import views

app_name = 'plan'

urlpatterns = [
    path('', views.PlanChoise.as_view(), name='plan_choise'),
]
