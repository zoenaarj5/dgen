import datetime
from django.db import models
from accounts.models import ArepUser


class Article(models.Model):
    title = models.CharField(max_length=150,null=True,unique=True)
    content = models.TextField(max_length=1000,null=True)
    creation_date = models.DateTimeField(default=datetime.datetime.now)
    publishing_date = models.DateTimeField(null=True)
    removal_date = models.DateTimeField(null=True)
    blocking_date = models.DateTimeField(null=True)
    author = models.ForeignKey(ArepUser,null=True,related_name="articles", on_delete=models.RESTRICT)
    def __str__(self):
        return self.title + "|" + self.publishing_date

class ReactionType(models.TextChoices):
    LIKE = "L", "J'aime"
    DO_NOT_LIKE = "NL", "Je n'aime pas" 
    FUNNY = "F", "Drôle"
    SAD = "S", "Triste"
    INDIFFERENT = "I", "Indifférent"
    NO_REACTION = "NR", "Pas de réaction"

class Reaction(models.Model):
    author = models.ForeignKey(ArepUser,null=True,related_name="reactions",on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=ReactionType.choices,default=ReactionType.NO_REACTION)
    def __str__(self):
        return self.type+"|"+self.author.first_name

class Comment(models.Model):
    article = models.ForeignKey(Article,related_name="comments",null=True,on_delete=models.CASCADE)
    author = models.ForeignKey(ArepUser,null=True,on_delete=models.CASCADE)
    content = models.TextField(max_length=1000,null=True)