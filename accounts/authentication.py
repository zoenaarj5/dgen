from django.contrib.auth.backends import ModelBackend
from .models import ArepUser
from django.db import models

class EmailOrPhoneBackend(ModelBackend):
    def authenticate(self, request, username = ..., password = ..., **kwargs):
        try:
            user = ArepUser.objects.get(
                models.Q(email=username) | models.Q(phone_number=username)
            )
            if user.check_password(password):
                return user
        except ArepUser.DoesNotExist:
            return None
