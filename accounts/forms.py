from django import forms
from .models import ArepUser
class ArepUserCreationForm(forms.ModelForm):
    email = forms.EmailField(required=False,label="Email")
    email_conf = forms.EmailField(required=False,label="Confirmer l'email")
    phone_number = forms.CharField(required=False,label="Tél.")
    phone_number_conf = forms.CharField(required=False,label="Confirmer Tél.")
    password = forms.CharField(label="mot de passe",widget = forms.PasswordInput)
    password_conf = forms.CharField(label="Confirmer mot de passe",widget=forms.PasswordInput)
    class Meta:
        model = ArepUser
        fields = ["email","phone_number","password"]

    def clean(self):
        cleaned_data = super().clean()
        email=cleaned_data.get("email")
        email_conf=cleaned_data.get("email_conf")
        password=cleaned_data.get("password")
        password_conf=cleaned_data.get("password_conf")
        phone_number=cleaned_data.get("phone_number")
        phone_number_conf=cleaned_data.get("phone_number_conf")

        if not cleaned_data.get("email") and not cleaned_data.get("phone_number"):
            raise forms.ValidationError("Vous devez fournir une addresse mail ou un numéro de téléphone.")

        if email and email_conf and email!=email_conf: 
            self.add_error("email_conf","L'adresse mail et la confirmation de l'adresse mail ne correspondent pas.") 
        if phone_number and phone_number_conf and phone_number!=phone_number_conf: 
            self.add_error("phone_number_conf","Le numéro de téléphone et la confirmation du numéro de téléphone ne correspondent pas.") 
        if password and password_conf and password!=password_conf: 
            self.add_error("password_conf","Le mot de passe et la confirmation du mot de passe ne correspondent pas.") 

        return cleaned_data
    
class LoginForm(forms.Form):
    username = forms.CharField(label = "Email / Tél")
    password = forms.CharField(widget = forms.PasswordInput)