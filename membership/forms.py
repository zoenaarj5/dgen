from django import forms
from .models import Member, Contact, Federation, Branch, Country,MemberCategory,MemberStatus,MaritalStatus,MemberTitle,Grade,Gender
from accounts.models import ArepUser 
class ContactForm(forms.ModelForm):
    vkFieldLabels={
        "street_name":"Nom de la rue",
        "street_nr":"Numéro",
        "street_box":"Boîte",
        "zip_code":"Code postal",
        "mobile_nr_1":"GSM (1)",
        "mobile_nr_2":"GSM (2)",
        "fixed_nr_1":"Tél. fixe (1)",
        "email_1":"Email (1)",
        "email_2":"Email (2)",
        "city":"Localité"
    }
    street_name = forms.CharField(label=vkFieldLabels["street_name"],required=False)
    street_nr = forms.CharField(label=vkFieldLabels["street_nr"],required=False)
    street_box = forms.CharField(label=vkFieldLabels["street_box"],required=False)
    zip_code = forms.CharField(label=vkFieldLabels["zip_code"],required=False)
    mobile_nr_1 = forms.CharField(label=vkFieldLabels["mobile_nr_1"],required=False)
    mobile_nr_2 = forms.CharField(label=vkFieldLabels["mobile_nr_2"],required=False)
    fixed_nr_1 = forms.CharField(label=vkFieldLabels["fixed_nr_1"],required=False)
    email_1 = forms.EmailField(label=vkFieldLabels["email_1"],required=False)
    email_2 = forms.EmailField(label=vkFieldLabels["email_2"],required=False)
    city = forms.CharField(label=vkFieldLabels["city"],required=False),

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
        for field,label in self.vkFieldLabels.items():
            self.fields[field].widget.attrs["placeholder"]=label

class MemberFormBis(forms.ModelForm):
    vkFieldLabels={
        "branch":"Antenne",
        "title":"Titre",
        "name":"Nom",
        "postname":"postnom",
        "first_name":"Prénom",
        "sex":"sexe",
        "birthdate":"Né(e) le",
        "sponsored":"Parrainé(e)",
        "sponsor":"Sponsor",
        "status":"Statut",
        "function":"Fonction",
        "roles":"Rôles",
        "category":"Catégorie",
        "profession":"Profession",
        "grade":"Diplôme",
        "marital_status":"Statut marital",
        "child_count":"Nombre d'enfants"
    }
    birthdate=forms.DateField(widget=forms.DateInput(attrs={"type":"date","class":"form-control"}))
    class Meta:
        model = Member
        fields = [
            "branch","title","name","postname","first_name","sex","birthdate","sponsored","sponsor","status","function","roles",
            "category","profession","grade","marital_status",
            "child_count"
        ]
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field,label in self.vkFieldLabels.items():
            self.fields[field].widget.attrs["placeholder"]=label

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
            "branch","title","name","postname","first_name","sex","birthdate","sponsored","sponsor","status","function","roles",
            "category","profession","grade","marital_status",
            "child_count"
        ]

class MemberEditForm(forms.ModelForm):
   
    class Meta:
        model = Member
        fields=[
            "branch","title","name","postname","first_name","sex","birthdate","sponsored","sponsor","status","function","roles",
            "category","profession","grade","marital_status",
            "child_count"
        ]
        
class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = ["name","description"]

class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ["code","name"]

class FederationForm(forms.ModelForm):
    class Meta:
        model = Federation
        fields = ["name","country","responsible","description"]