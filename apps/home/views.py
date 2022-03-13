from django.shortcuts import render, redirect
from django.http import HttpResponse
from customer.views import check_login


# Create your views here.
def index(request):
    if check_login(request) is False:
        return redirect('customer:login')
    return render(request, 'home/content.html')
