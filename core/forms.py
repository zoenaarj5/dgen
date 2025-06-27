from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = ["email","phone_number","password"]
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        phone = cleaned_data.get("phone_number")
        if not email and not phone:
            raise forms.ValidationError("Veuillez entrer l'email ou le numéro de téléphone.")
        return cleaned_data

class EmailOrPhoneLoginForms(forms.Form):
    username = forms.CharField(label="Email ou Numéro de téléphone")
    password = forms.CharField(widget = forms.PasswordInput)