import datetime
from django.db import models
from accounts.models import ArepUser
from membership.models import Federation
from django.utils import timezone

class Event(models.Model):
    creation_date = models.DateTimeField(default=timezone.now)
    start_date = models.DateTimeField(null=True,blank=True)
    end_date = models.DateTimeField(null=True,blank=True)
    title = models.CharField(null=True,blank=True,max_length=100)
    intro = models.TextField(null=True,blank=True,max_length=500)
    content = models.TextField(null=True,blank=True,max_length=2000)
    author = models.ForeignKey(ArepUser,null=True,related_name="events",on_delete=models.RESTRICT)
    federation = models.ForeignKey(Federation,null=True,related_name="events",on_delete=models.RESTRICT)