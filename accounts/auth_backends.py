from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from django.db.models import Q
UserModel=get_user_model()

class PhoneEmailBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        user = None
        try:
            user = UserModel.objects.get(Q(email=username) | Q(phone_number=username))
        except UserModel.DoesNotExist:
            return None
        if user and user.check_password(password) and self.user_can_authenticate(user):
            return user
        
        return None
    
    def user_can_authenticate(self, user):
        return getattr(user,'is_active',False)
          