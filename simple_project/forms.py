from django import forms
from django.forms import ModelForm, fields, widgets

class MyForm(forms.Form): #Note that it is not inheriting from forms.ModelForm
    x = forms.IntegerField()
    y = forms.IntegerField()
    #All my attributes here