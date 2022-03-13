from django.shortcuts import render
from django.views import View
from .forms import OrderForm
from .models import Order
from plan.models import Plan


# Create your views here.
class OrderChoise(View):
    def get(self, request, plan_id):
        print("======================= plan_id")
        print(plan_id)
        print("======================= plan_id _End")
        # get plan
        plan = Plan.objects.get(id=plan_id)
        order_form = OrderForm()
        order_form['plan_id'].initial = plan_id
        
        context = {'plan': plan, 'order_form': order_form}
        return render(request, 'order/order.html', context)
    
    def post(self, request, plan_id):
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order = order_form.save(request)
            if order:
                return render(request, 'order/order_success.html')
        plan = Plan.objects.get(id=plan_id)
        context = {'plan': plan, 'order_form': order_form}
        return render(request, 'order/order.html', context)