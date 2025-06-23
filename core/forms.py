from django import forms

class EmailOrPhoneLoginForms(forms.Form):
    username = forms.CharField(label="Email ou Numéro de téléphone")
    password = forms.CharField(widget = forms.PasswordInput)