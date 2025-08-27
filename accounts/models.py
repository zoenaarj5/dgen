from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from datetime import datetime,timedelta
from django.utils import timezone
class ArepUserManager(BaseUserManager):

    def create_user(self, email=None,phone_number=None, password = None, **extra_fields):
        if not email and not phone_number:
            raise ValueError("Les utilisateurs doivent avoir une adresse email ou un numéro de téléphone.")
        
        email = self.normalize_email(email) if email else None
        
        user = self.model(email=email,phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff",True)
        extra_fields.setdefault("is_superuser",True)

        if not email:
            raise ValueError("Superusers must have an email address.")

        return self.create_user(email=email,password=password,**extra_fields)

class ArepUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True,null=True,blank=True)
    phone_number = models.CharField(max_length=15,unique=True,null=True,blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = ArepUserManager()

    def __str__(self):
        return self.email or self.phone_number or "Anonymous"

def default_expiry():
    return timezone.now()+timedelta(minutes=10)

class ArepUserPasswordRecoveryRequest():
    creation_date = models.DateTimeField(blank=True,default=timezone.now)
    expiry_date = models.DateTimeField(null=True,blank=True,default=default_expiry)
    user = models.ForeignKey(ArepUser,on_delete=models.CASCADE)
    accepted = models.BooleanField(default=False)