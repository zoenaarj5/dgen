from django import forms
from .models import Member, Contact, Federation, Branch, Country
from accounts.models import ArepUser 
class ContactForm(forms.ModelForm):
    street_name = forms.CharField(label="Nom de la rue")
    street_number = forms.CharField(label="Numéro")
    street_box = forms.CharField(label="Boîte")
    zip_code = forms.CharField(label="Code postal")
    mobile_nr_1 = forms.CharField(label="Nr GSM (1)")
    mobile_nr_2 = forms.CharField(label="Nr GSM (2)")
    fixed_nr_1 = forms.CharField(label="Nr tél. fixe")
    email_1 = forms.EmailField(label="Email (1)")
    email_2 = forms.EmailField(label="Email (2)")
    city = forms.CharField(label="Localité")
    class Meta:
        model = Contact
        fields = [
            "street_name","street_nr","street_box","zip_code",
            "mobile_nr_1","mobile_nr_2","fixed_nr_1",
            "email_1","email_2","city","country"
                  ]
        labels={
            "country":"Pays"
        }
        widgets = {
            "country": forms.Select(attrs={"class":"form-select"})
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields["category"].queryset=Country.objects.all

class ArepUserForm(forms.ModelForm):
    email = forms.EmailField(required=False,label="Email")
    email_conf = forms.EmailField(required=False,label="Confirmer email")
    phone_number = forms.CharField(required=False,max_length=15,label="Tél.")
    phone_number_conf = forms.CharField(required=False,max_length=15,label="Confirmer tél.")
    password = forms.CharField(widget=forms.PasswordInput, label = "Mot de passe")
    password_conf = forms.CharField(widget=forms.PasswordInput,label="Confirmer mot de passe") 
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
            "branch","name","postname","first_name","sex","sponsored","sponsor","status","function","roles",
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