from django import forms
from .models import Member, Contact, Federation, Branch
from accounts.models import ArepUser 
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            "street_name","street_nr","street_box","zip_code",
            "mobile_nr_1","mobile_nr_2","fixed_nr_1",
            "email_1","email_2","city","country"
                  ]

class ArepUserForm(forms.ModelForm):
    email_conf = forms.EmailField(label="Confirmer email")
    phone_number_conf = forms.CharField(max_length=15,label="Confirmer tél.")
    password_conf = forms.CharField(widget=forms.PasswordInput,label="Confirmer mot de passe") 
    password = forms.CharField(widget=forms.PasswordInput, label = "Mot de passe")
    class Meta:
        model = ArepUser
        fields = [
            "email","email_conf","phone_number","phone_number_conf",
            "password","password_conf"
        ]

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
#        fields = ["email","name","postname","first_name","sex","birthdate","registration_start_date","registration_end_date","sponsored","function","category","profession","marital_status","child_count","branch_id","grade_id","sponsor_id","status"]
        fields=[
            "user","branch","name","postname","first_name","sex","registration_start_date",
            "registration_end_date","sponsored","sponsor","status","function","roles",
            "category","profession","grade","marital_status",
            "child_count"
        ]

class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = ["name","description"]

class FederationForm(forms.ModelForm):
    class Meta:
        model = Federation
        fields = ["name","country","responsible","description"]