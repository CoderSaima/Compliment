from django import forms

class Form(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
