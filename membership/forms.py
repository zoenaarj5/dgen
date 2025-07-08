from django import forms
from .models import Member, Contact, Federation, Branch, Country,MemberCategory,MemberStatus,MaritalStatus,MemberTitle,Grade,Gender
from accounts.models import ArepUser 
class ContactForm(forms.ModelForm):
    street_name = forms.CharField(label="Nom de la rue")
    street_nr = forms.CharField(label="Numéro")
    street_box = forms.CharField(label="Boîte")
    zip_code = forms.CharField(label="Code postal")
    mobile_nr_1 = forms.CharField(label="Nr GSM (1)")
    mobile_nr_2 = forms.CharField(label="Nr GSM (2)")
    fixed_nr_1 = forms.CharField(label="Nr tél. fixe")
    email_1 = forms.EmailField(label="Email (1)")
    email_2 = forms.EmailField(label="Email (2)")
    city = forms.CharField(label="Localité"),

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
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields["country"].label="Pays"
        self.fields["country"].queryset = Country.objects.order_by("name")

class MemberForm(forms.ModelForm):
    title = forms.ChoiceField(
        choices=MemberTitle.choices,
        initial=MemberTitle.UNKNOWN,
        widget=forms.Select(),
    )
    name=forms.CharField(label="Nom")
    postname=forms.CharField(label="Postnom")
    first_name=forms.CharField(label="Prénom")
    sex=forms.ChoiceField(
        choices = Gender.choices,
        initial = Gender.UNKNOWN,
        widget=forms.Select(attrs={"class":"form-control"}),
        label="Sexe"
    )
    sponsored=forms.CheckboxInput()
    status=forms.ChoiceField(
        choices=MemberStatus.choices,
        initial=MemberStatus.NON_ACTIVE,
        label="Statut"
    )
    function=forms.CharField(label="Fonction")
    roles=forms.CharField(label="Rôles")
    category=forms.ChoiceField(
            choices=MemberCategory.choices,
            initial=MemberCategory.ORDINARY,
            widget=forms.Select(attrs={"class":"form-control"}),
            label="Catégorie"
    )
    profession=forms.CharField(label="Profession")
    grade=forms.ChoiceField(
        choices = Grade.choices,
        initial = Grade.NONE,
        widget=forms.Select(attrs={"class":"form-control"}),
        label = "Diplôme"
    )
    marital_status=forms.ChoiceField(
        choices = MaritalStatus.choices,
        initial = MaritalStatus.UNKNOWN,
        widget=forms.Select(attrs={"class":"form-control"}),
        label="Statut marital"
    )
    child_count=forms.NumberInput()
    class Meta:
        model = Member
        fields=[
            "branch","title","name","postname","first_name","sex","sponsored","sponsor","status","function","roles",
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