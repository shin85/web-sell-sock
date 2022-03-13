# from multiprocessing.dummy import active_children
from django.contrib import admin
from django import forms
from .models import Customer, History
from django.utils.translation import gettext_lazy as _
from django.utils.translation import activate, get_language, get_language_info
from .common import Common


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    # list_display format number balanced
    def balance_display(self, obj):
        return '{:,}'.format(obj.balance)
    balance_display.short_description = "Số dư (VNĐ)"
    
    list_display = ('username', 'email', 'balance_display')
    
    # Search by customer_id
    search_fields = ['username', 'email']
    
    # Filter by customer_id
    list_filter = ('username', 'email',)
    
    # Sort by created_at
    ordering = ('username',)
    
    # Show 10 items per page
    list_per_page = 20

    # get form
    def get_form(self, request, obj=None, **kwargs):
        form = super(CustomerAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['password'].widget = forms.PasswordInput()
        # when editing
        if obj:
            # field readonly
            form.base_fields['username'].widget.attrs['readonly'] = True
            # field help_text
            form.base_fields['username'].help_text = _(
                'Username cannot be changed.')
            form.base_fields['password'].help_text = _(
                'Empty password if not change.')
        # when creating
        else:
            # field required
            form.base_fields['password'].required = True
        # hide field salt
        form.base_fields['salt'].widget = forms.HiddenInput()
        
        return form

    # save customer
    def save_model(self, request, obj, form, change):
        # customer update
        if change:
            if not obj.password:
                # get password in database
                old_password = Customer.objects.get(id=obj.id).password
                obj.password = old_password
            else:
                obj.password, obj.salt = Common.md5_password(obj.password)
            obj.save()
        # customer create
        else:
            obj.password, obj.salt = Common.md5_password(obj.password)
            obj.save()


@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    def balance_change_display(self, obj):
        return '{:,}'.format(obj.balance_change)
    balance_change_display.short_description = "Số tiền (VNĐ)"
    
    def balance_after_display(self, obj):
        return '{:,}'.format(obj.balance_after)
    balance_after_display.short_description = "Số dư sau (VNĐ)"
    
    def balance_before_display(self, obj):
        return '{:,}'.format(obj.balance_before)
    balance_before_display.short_description = "Số dư trước (VNĐ)"
    
    
    list_display = ('id', 'customer', 'description', 'balance_change_display', 'balance_before_display', 'balance_after_display', 'create_at')
    list_display_links = None

    # Search by customer_id
    search_fields = ['customer__username', 'customer__email', 'description']
    
    # Filter by customer_id
    list_filter = ('customer__username', 'customer__email',)
    
    # Sort by created_at
    ordering = ('-create_at',)
    
    # Show 10 items per page
    list_per_page = 20
    
    # Disable add new
    def has_add_permission(self, request):
        return False
    
    # Disable delete
    def has_delete_permission(self, request, obj=None):
        return False
    