from django import forms
from .models import ArepUser
from django.contrib.auth import authenticate

class ArepUserCreationForm(forms.ModelForm):
    vkFieldLabels={
        "email"             :       "Email"                         ,
        "email_conf"        :       "Confirmer l'email"             ,
        "phone_number"      :       "Tél"                           ,
        "phone_number_conf" :       "Confirmer tél."                ,
        "password"          :       "Mot de passe"                  ,
        "password_conf"     :       "Confirmer le mot de passe"
    }
    email = forms.EmailField(required=False,label=vkFieldLabels["email"])
    email_conf = forms.EmailField(required=False,label=vkFieldLabels["email_conf"])
    phone_number = forms.CharField(required=False,label=vkFieldLabels["phone_number"])
    phone_number_conf = forms.CharField(required=False,label=vkFieldLabels["phone_number_conf"])
    password = forms.CharField(label=vkFieldLabels["password"],widget = forms.PasswordInput())
    password_conf = forms.CharField(label=vkFieldLabels["password_conf"],widget=forms.PasswordInput())

    class Meta:
        model = ArepUser
        fields = ["email","email_conf","phone_number","phone_number_conf","password","password_conf"]

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        
        # Adding placeholders on fields
        for field,label in self.vkFieldLabels.items():
            self.fields[field].widget.attrs["placeholder"]=label

    def save(self,commit=True):
        user = super().save(commit=False)
        raw_password=self.cleaned_data["password"]
        user.set_password(raw_password)
        if commit:
            user.save()
        return user

    def clean(self):
        cleaned_data = super().clean()
        email=cleaned_data.get("email")
        email_conf=cleaned_data.get("email_conf")
        password=cleaned_data.get("password")
        password_conf=cleaned_data.get("password_conf")
        phone_number=cleaned_data.get("phone_number")
        phone_number_conf=cleaned_data.get("phone_number_conf")

        if not email and not phone_number:
            raise forms.ValidationError("Vous devez fournir une addresse mail ou un numéro de téléphone.")

        if email and email_conf and email!=email_conf:
            self.add_error("email_conf","L'adresse mail et la confirmation de l'adresse mail ne correspondent pas.")
        if phone_number and phone_number_conf and phone_number!=phone_number_conf:
            self.add_error("phone_number_conf","Le numéro de téléphone et la confirmation du numéro de téléphone ne correspondent pas.")
        if password and password_conf and password!=password_conf:
            self.add_error("password_conf","Le mot de passe et la confirmation du mot de passe ne correspondent pas.")

        return cleaned_data
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field,label in self.vkFieldLabels.items():
            self.fields[field].widget.attrs["placeholder"]=label
    
class ArepUserEditForm(forms.ModelForm):
    vkFieldLabels={
        "email"             :       "Email"                         ,
        "email_conf"        :       "Confirmer l'email"             ,
        "phone_number"      :       "Tél"                           ,
        "phone_number_conf" :       "Confirmer tél."                ,
        "password"          :       "Mot de passe"                  ,
        "password_conf"     :       "Confirmer le mot de passe"
    }
    email = forms.EmailField(required=False,label=vkFieldLabels["email"])
    email_conf = forms.EmailField(required=False,label=vkFieldLabels["email_conf"])
    phone_number = forms.CharField(required=False,label=vkFieldLabels["phone_number"])
    phone_number_conf = forms.CharField(required=False,label=vkFieldLabels["phone_number_conf"])
    password = forms.CharField(label=vkFieldLabels["password"],widget = forms.PasswordInput())
    password_conf = forms.CharField(label=vkFieldLabels["password_conf"],widget=forms.PasswordInput())
    class Meta:
        model = ArepUser
        fields = ["email","email_conf","phone_number","phone_number_conf","password","password_conf"]

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        
        # Adding placeholders on fields
        for field,label in self.vkFieldLabels.items():
            self.fields[field].widget.attrs["placeholder"]=label

class LoginForm(forms.Form):
    username = forms.CharField(label = "Email / Tél")
    password = forms.CharField(label = "Mot de passe",widget = forms.PasswordInput)
    
    def __init__(self, *args, **kwargs):
        self.user = None
        super().__init__(*args,**kwargs)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        if username and password:
            self.user = authenticate(username = username, password = password)
            if self.user is None:
                raise forms.ValidationError("L'email et/ou le mot de passe n'est pas valide.")
        return cleaned_data
    def get_user(self):
        return self.user 

    