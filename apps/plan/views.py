from django.shortcuts import render, redirect
from django.views import View
from .forms import PlanForm
from .models import Plan
from customer.views import check_login

# Create your views here.
class PlanChoise(View):
    def get(self, request):
        if check_login(request) is False:
            return redirect('customer:login')
        # get plan
        plans = Plan.objects.filter(active=True, name__gt=1)
        context = {'plans': plans}
        return render(request, 'plan/plan_choise.html', context)
        
        