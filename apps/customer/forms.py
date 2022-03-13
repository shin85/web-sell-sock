from django import forms
from django.utils.translation import gettext_lazy as _
from django.utils.translation import activate, get_language, get_language_info
import re
from .models import Customer
from .common import Common
from django.db.models import Q

class CustomerRegisterForm(forms.Form):
    username = forms.CharField(label = _('Tài khoản'), max_length=255, widget=forms.TextInput(attrs={'class': 'form-control form-control-solid h-auto py-6 px-6 rounded-lg font-size-h6', 'placeholder': _('Tài khoản')}))
    email = forms.EmailField(label = _('Email'), max_length=255, widget=forms.EmailInput(attrs={'class': 'form-control form-control-solid h-auto py-6 px-6 rounded-lg font-size-h6', 'placeholder': _('Email')}))
    password = forms.CharField(label = _('Mật khẩu'), max_length=255, widget=forms.PasswordInput(attrs={'class': 'form-control form-control-solid h-auto py-6 px-6 rounded-lg font-size-h6', 'placeholder': _('Mật khẩu')}))
    password_re = forms.CharField(label = _('Nhập lại mật khẩu'), max_length=255, widget=forms.PasswordInput(attrs={'class': 'form-control form-control-solid h-auto py-6 px-6 rounded-lg font-size-h6', 'placeholder': _('Nhập lại mật khẩu')}))
    
    # validate username
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not re.match(r'^[a-zA-Z0-9_]+$', username):
            raise forms.ValidationError(_('Tài khoản chỉ chứa A-Z, a-z, 0-9 và dấu gạch dưới "_".'), code='username_invalid')
        if len(username) < 6:
            raise forms.ValidationError(_('Tài khoản phải có ít nhất 6 kí tự.'), code='username_less')
        if Customer.objects.filter(username=username):
            raise forms.ValidationError(_('Tài khoản đã tồn tại.'), code='username_exists')
        return username

    # validate password
    def clean_password(self):
        password = self.cleaned_data['password']
        if re.search(r'[^a-zA-Z0-9_]', password):
            raise forms.ValidationError(_('Mật khẩu chỉ chứa A-Z, a-z, 0-9 và dấu gạch dưới "_".'), code='password_invalid')
        if len(password) < 6:
            raise forms.ValidationError(_('Mật khẩu phải có ít nhất 6 kí tự.'), code='password_less')
        return password
    
    # validate re-password
    def clean_password_re(self):
        password = self.cleaned_data.get('password')
        password_re = self.cleaned_data.get('password_re')
        if password != password_re:
            raise forms.ValidationError(_('Mật khẩu và nhập lại mật khẩu không khớp.'), code='password_re_invalid')
        return password_re
    
    # validate email
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Customer.objects.filter(email=email):
            raise forms.ValidationError(_('Email đã tồn tại.'), code='email_exists')
        return email
    
    # save customer
    def save(self):
        customer = Customer()
        customer.username = self.clean_username()
        customer.email = self.clean_email()
        password = self.clean_password()
        customer.password, customer.salt = Common.md5_password(password)
        self.clean_password_re()
        customer.save()
        return customer

class CustomerLoginForm(forms.Form):
    username = forms.CharField(label = _('Tài khoản hoặc Email'), max_length=255, widget=forms.TextInput(attrs={'class': 'form-control form-control-solid h-auto py-6 px-6 rounded-lg', 'placeholder': _('Nhập tài khoản hoặc Email')}))
    password = forms.CharField(label = _('Mật khẩu'), max_length=255, widget=forms.PasswordInput(attrs={'class': 'form-control form-control-solid h-auto py-6 px-6 rounded-lg', 'placeholder': _('Nhập mật khẩu')}))
    
    def check_username(self):
        username = self.cleaned_data.get('username')
        customer = Customer.objects.filter(Q(username=username) | Q(email=username))
        if not customer:
            self.add_error('username', _('Tài khoản không tồn tại.'))
            return False
        return customer
    
    def check_password(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        customer = Customer.objects.filter(username=username)
        password_input_general = Common.md5_password(password, customer[0].salt)
        if password_input_general[0] != customer[0].password:
            self.add_error('password', _('Mật khẩu không đúng.'))
            return False
        return customer
        
    
    # login customer
    def login(self):
        customer = self.check_username()
        if customer:
            customer = self.check_password()
        return customer

class CustomerInfoForm(forms.Form):
    password_cur = forms.CharField(label = _('Mật khẩu hiện tại'), max_length=255, widget=forms.PasswordInput(attrs={'class': 'form-control form-control-solid h-auto py-6 px-6 rounded-lg font-size-h6', 'placeholder': _('Mật khẩu hiện tại')}))
    password = forms.CharField(label = _('Mật khẩu mới'), max_length=255, widget=forms.PasswordInput(attrs={'class': 'form-control form-control-solid h-auto py-6 px-6 rounded-lg font-size-h6', 'placeholder': _('Mật khẩu mới')}))
    password_re = forms.CharField(label = _('Nhập lại mật khẩu mới'), max_length=255, widget=forms.PasswordInput(attrs={'class': 'form-control form-control-solid h-auto py-6 px-6 rounded-lg font-size-h6', 'placeholder': _('Nhập lại mật khẩu mới')}))

    # validate password_cur
    def check_password_cur(self, request):
        customer = Customer.objects.get(pk=request.session['customer']['id'])
        password_cur = self.cleaned_data.get('password_cur')
        password_cur_md5 = Common.md5_password(password_cur, customer.salt)
        if password_cur_md5[0] != customer.password:
            self.add_error('password_cur', _('Mật khẩu hiện tại không đúng.'))
            return False
        return password_cur
    
    # validate password
    def clean_password(self):
        password = self.cleaned_data['password']
        if re.search(r'[^a-zA-Z0-9_]', password):
            raise forms.ValidationError(_('Mật khẩu mới chỉ chứa A-Z, a-z, 0-9 và dấu gạch dưới "_".'), code='password_invalid')
        if len(password) < 6:
            raise forms.ValidationError(_('Mật khẩu mới phải có ít nhất 6 kí tự.'), code='password_less')
        return password
    
    # validate re-password
    def clean_password_re(self):
        password = self.cleaned_data.get('password')
        password_re = self.cleaned_data.get('password_re')
        if password != password_re:
            raise forms.ValidationError(_('Mật khẩu mới và nhập lại mật khẩu mới không khớp.'), code='password_re_invalid')
        return password_re
    
    # save customer
    def update(self, request):
        error_flag = False
        customer = Customer.objects.get(pk=request.session['customer']['id'])
        password_cur = self.check_password_cur(request)
        if password_cur is False:
            error_flag = True
        password = self.clean_password()
        password_new, salt_new = Common.md5_password(password)
        if error_flag == False:
            customer.password = password_new
            customer.salt = salt_new
            customer.save()
            # customer.update(password=password_new, salt=salt_new)
        return customer