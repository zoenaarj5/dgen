from django.db import models
from accounts.models import ArepUser
from datetime import datetime

class Gender(models.TextChoices):
    MALE = "M", "Homme"
    FEMALE = "F", "Femme"
    UNKNOWN = "U", "Inconnu"

class MaritalStatus(models.TextChoices):
    SINGLE = "S", "Célibataire"
    MARRIED = "M", "Marié(e)"
    COHABITANT = "C", "Cohabitant"
    WIDOW = "W", "Veuf(ve)"
    UNKNOWN = "U", "Inconnu"

class MemberCategory (models.TextChoices):
    HONOR = "H", "Membre d'honneur"
    ORDINARY = "O", "Membre ordinaire"
    
class Country(models.Model):
    code = models.CharField(max_length=3,primary_key=True)
    name = models.CharField(max_length=50,unique=True)
    def __str__(self):
        return self.code + " " + self.name
    
class Permission (models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=150)
    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=150)
    permissions = models.ManyToManyField(Permission,related_name="permissions")
    def __str__(self):
        return self.name

class Federation (models.Model):
    name = models.CharField(max_length=100,unique=True)
    country = models.ForeignKey(Country,on_delete=models.RESTRICT,null=True)
    responsible = models.CharField(max_length=100,null=True)
    def __str__(self):
        return str(self.id) + " " + self.name

class Branch (models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    federation = models.ForeignKey(Federation,on_delete=models.RESTRICT,related_name="branches",null=True)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields = ["federation","name"],name = "unique_federation_branch")
        ]
    def __str__(self):
        return self.name + " (" + self.federation.name + ")"

class PersonType (models.Model):
    code = models.CharField(max_length=1,primary_key=True)
    name = models.CharField(max_length=20,unique=True)
    def __str__(self):
        return self.code + " " + self.name

class MemberTitle (models.Model):
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=150)
    def __str__(self):
        return self.code + " " + self.name
    
class MemberStatus (models.TextChoices):
    ACTIVE =        "AC","Actif"
    NON_ACTIVE =    "NA","Inactif"
    SUSPENDED =     "SP","Suspendu"
    PENDING =       "PD","En attente"
    IN_COURSE =     "IC","Inscription en cours"
    REMOVED =       "RM","Radié"

class Grade (models.TextChoices):
    NONE        =   "N",    "Aucun"
    BREVET      =   "BV",    "Brevet"
    HIGH_SCHOOL =   "HS",    "Baccalauréat"
    BACHELOR    =   "BC",    "Bachelier"
    GRADUAT     =   "GD",    "Graduat"
    LICENSE     =   "LC",    "Licence"
    MASTER      =   "MA",    "Master"
    PHD         =   "PH",    "Doctorat"
    ENGINEER    =   "EN",    "Ingénieur"
    

class Contact (models.Model):
    street_name = models.CharField(max_length=150)
    street_nr = models.CharField(max_length=10)
    street_box = models.CharField(max_length=10)
    zip_code = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    country = models.ForeignKey(Country,null=True,on_delete=models.RESTRICT)
    mobile_nr_1 = models.CharField(max_length=20)
    mobile_nr_2 = models.CharField(max_length=20)
    fixed_nr_1 = models.CharField(max_length=20)
    email_1 = models.EmailField(max_length=50)
    email_2 = models.EmailField(max_length=50)
    def __str__(self):
        return self.id + " " + self.mobile_nr_1 + " " + self.email_1

class Member (models.Model):
    user = models.ForeignKey(ArepUser,null=True,related_name="members", on_delete=models.RESTRICT)
    branch = models.ForeignKey(Branch,on_delete=models.RESTRICT,null=True,related_name="members")
    name = models.CharField(max_length=100)     
    postname = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    sex = models.CharField(max_length=10,choices = Gender.choices,default=Gender.UNKNOWN)
    birthdate = models.DateField()
    registration_start_date = models.DateTimeField(null=True,default=datetime.now)
    registration_end_date = models.DateTimeField(null=True)
    sponsored = models.BooleanField(default=False)
    sponsor = models.ForeignKey("self",name="sponsor",on_delete=models.RESTRICT,null=True)
    status = models.CharField(max_length=10,choices=MemberStatus.choices,default=MemberStatus.NON_ACTIVE)
    function = models.CharField(max_length=100,null=True)
    roles = models.CharField(max_length=100,null=True)
    category = models.CharField(max_length=10,choices=MemberCategory.choices,default=MemberCategory.ORDINARY)
    profession = models.CharField(max_length=50,null=True)
    grade = models.CharField(max_length=20,choices=Grade.choices,default=Grade.NONE)
    marital_status = models.CharField(max_length=10,choices=MaritalStatus.choices,default=MaritalStatus.UNKNOWN)
    child_count = models.IntegerField(default=0)
    contact = models.OneToOneField(Contact,null=True,on_delete=models.RESTRICT)
    def __str__(self):
        return self.first_name + " | " + self.name + " | " + self.postname

