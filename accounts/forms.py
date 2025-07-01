from django import forms
from .models import ArepUser
class ArepUserCreationForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)

    class Meta:
        model = ArepUser
        fields = ["email","phone_number","password"]

    def clean(self):
        cleaned_data = super().clean()
        if not cleaned_data.get("email") and not cleaned_data.get("phone_number"):
            raise forms.ValidationError("Vous devez fournir une addresse mail ou un numéro de téléphone.")
        return cleaned_data
    
class LoginForm(forms.Form):
    username = forms.CharField(label = "Email / Tél")
    password = forms.CharField(widget = forms.PasswordInput)