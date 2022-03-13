from django.contrib import admin
from .models import Plan
from django import forms
from django.utils.translation import gettext_lazy as _

# Register your models here.
@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'duration', 'time_min', 'active')
    
    # get form
    def get_form(self, request, obj=None, **kwargs):
        form = super(PlanAdmin, self).get_form(request, obj, **kwargs)
        # name require
        form.base_fields['name'].required = True
        # price required
        form.base_fields['price'].required = True
        # description required
        form.base_fields['description'].required = True
        # duration required
        form.base_fields['duration'].required = True
        # duration help_text
        form.base_fields['duration'].help_text = _('Thời gian sử dụng: phút<br />0: Không giới hạn<br />')
        # time_min required
        form.base_fields['time_min'].required = True
        # active checkbox
        form.base_fields['active'].widget = forms.CheckboxInput()
        return form
    
    # save customer
    def save_model(self, request, obj, form, change):
        # Plan update
        if change:
            # obj.name = Plan.objects.get(id=obj.id).name
            obj.save()
        # Plan create
        else:
            # obj.name = Plan.objects.get(id=obj.id).name
            obj.save()