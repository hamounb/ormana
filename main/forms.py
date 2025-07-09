from django import forms
from django.core.exceptions import ValidationError


def is_mobile(value):
    if not str(value).isnumeric() or len(value) !=11 or str(value)[0] != '0':
        raise ValidationError('شماره موبایل صحیح نمی‌باشد!')
    

class ContactUsForm(forms.Form):
    name = forms.CharField(max_length=200, label="نام و نام خانوادگی", required=True)
    mobile = forms.CharField(max_length=11, label="شماره تماس", required=True, validators=[is_mobile])
    text = forms.CharField(max_length=255, label="پیام", required=True, widget=forms.Textarea)