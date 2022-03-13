from django import forms
from .models import Order
from plan.models import Plan
from customer.models import Customer, History


class OrderForm(forms.Form):
    plan_id = forms.IntegerField(label='Gói', widget=forms.HiddenInput())
    amount = forms.IntegerField(label='Số lượng', widget=forms.NumberInput(
        attrs={'class': 'form-control form-control-solid h-auto py-1 px-1 rounded-lg font-size-h6', 'placeholder': 'Số lượng', 'min': '1'}))

    # def check_plan_id
    def check_plan_id(self):
        plan_id = self.cleaned_data.get('plan_id')
        plan = Plan.objects.get(pk=plan_id)
        if not plan:
            self.add_error('plan_id', 'Gói Sock5 không tồn tại.')
            return False
        return plan
    
    # def check_customer_id
    def check_customer_id(self, request):
        customer_id = request.session['customer']['id']
        customer = Customer.objects.get(pk=customer_id)
        if not customer:
            self.add_error('customer_id', 'Khách hàng không tồn tại.')
            return False
        return customer

    # def clean_amount
    def check_amount(self, request):
        amount = self.cleaned_data.get('amount')
        if amount <= 0:
            self.add_error('amount', 'Số lượng phải lớn hơn 0.')
            return False
        plan = self.check_plan_id()
        customer = self.check_customer_id(request)
        price_total = plan.price * amount
        
        if price_total > customer.balance:
            self.add_error('amount', 'Số dư không đủ mua.')
            return False, False, False
        
        balance_before = customer.balance
        balance_after = customer.balance - price_total
        
        return amount, balance_after, balance_before
    
    # def save
    def save(self, request):
        error_flag = False
        order = Order()
        
        customer = self.check_customer_id(request)
        if customer is False:
            error_flag = True
        if error_flag is False:
            plan = self.check_plan_id()
            if plan is False:
                error_flag = True
        if error_flag is False:
            amount, balance_after, balance_before = self.check_amount(request)
            if amount is False:
                error_flag = True
        
        if error_flag is False:
            order.plan_id = plan
            order.customer_id = customer
            order.amount = amount
            balance_change = plan.price* amount
            order.price_total = balance_change
            order.balance_after = balance_after
            order.balance_before = balance_before
            order.save()
        
            customer.balance = balance_after
            customer.save()
            
            description = "Mua: x"+ str(amount) + "" + plan.name
            History.save_history(customer, description, -balance_change, balance_before, balance_after)
        
            return order