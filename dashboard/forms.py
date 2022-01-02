from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields 
from .models import orders_done, reportData

class reportDataForm(forms.ModelForm):
    class Meta:
        model = reportData
        fields = '__all__'

class OrderForm(forms.ModelForm):
    class Meta:
        model = orders_done
        fields = ['staff', 'order']