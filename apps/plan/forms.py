from django import forms

class PlanForm(forms.Form):
    name = forms.CharField(label='Tên gói', max_length=100)
    price = forms.IntegerField(label='Giá', min_value=0)
    description = forms.CharField(label='Mô tả', max_length=500)
    duration = forms.IntegerField(label='Thời gian sử dụng', min_value=0)
    time_min = forms.IntegerField(label='Sử dụng tối thiểu', min_value=0)
    
    