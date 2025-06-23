from django import forms
from .models import Member, Contact
from .models import RpUser 
class AddressForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ["street","street_number","street_box","zip_code","city","country_code"]

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ["email","name","postname","first_name","sex","birthdate","registration_start_date","registration_end_date","sponsored","function","category","profession","marital_status","child_count","branch_id","grade_id","sponsor_id","status_id"]

class RpUserForm(forms.ModelForm):
    class Meta:
        model = RpUser
        fields = ["email","phone_number","password"]