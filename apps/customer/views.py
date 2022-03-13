from django.shortcuts import render, redirect
from django.utils.translation import gettext_lazy as _
from . forms import CustomerLoginForm, CustomerRegisterForm, CustomerInfoForm
from django.views import View
from django.contrib import messages

def check_login(request):
    if request.session.get('customer', False) is False:
        return False
    return True

class CustomerLogin(View):
    def get(self, request):
        if request.session.get('customer', False):
            return redirect('/')
        form = CustomerLoginForm()
        context = {'form': form}
        return render(request, 'customer/login.html', context)
    
    def post(self, request):
        form = CustomerLoginForm(request.POST)
        if form.is_valid():
            customer = form.login()
            if form.errors:
                context = {'form': form}
                return render(request, 'customer/login.html', context)
            else:
                request.session['customer'] = {
                    'id': customer[0].id,
                    'username': customer[0].username,
                    'email': customer[0].email
                }
                return redirect('/')
        else:
            context = {'form': form}
            return render(request, 'customer/login.html', context)
    
class CustomerRegister(View):
    def get(self, request):
        if request.session.get('customer', False):
            return redirect('/')
        form = CustomerRegisterForm()
        context = {'form': form}
        return render(request, 'customer/register.html', context)
    
    def post(self, request):
        form = CustomerRegisterForm(request.POST)
        if form.is_valid():
            customer = form.save()
            if customer:
                request.session['customer'] = form.cleaned_data['username']
            return redirect('customer:login')
        else:
            context = {'form': form}
            return render(request, 'customer/register.html', context)

class CustomerPasswordLost(View):
    def get(self, request):
        return render(request, 'customer/password_lost.html')
    
    def post(self, request):
        return render(request, 'customer/password_lost.html')

class CustomerLogout(View):
    def get(self, request):
        if request.session.get('customer', False):
            del request.session['customer']
        return redirect('customer:login')

class CustomerInfo(View):
    def get(self, request):
        if check_login(request) is False:
            return redirect('customer:login')
        form = CustomerInfoForm()
        context = {'form': form, 'customer': request.session['customer']}
        return render(request, 'customer/info.html', context)
    
    def post(self, request):
        form = CustomerInfoForm(request.POST)
        if form.is_valid():
            customer = form.update(request)
            if not form.errors:
                messages.success(request, _('Đổi mật khẩu thành công'))
        
        context = {'form': form, 'customer': request.session['customer']}
        return render(request, 'customer/info.html', context)

def index(request):
    return redirect('customer:login')
