from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Votings(models.Model):
    voting_name = models.TextField()
    user_create = models.TextField()


class InformationAboutVoting(models.Model):
    information = models.TextField()
    labels = models.TextField()
    result = models.TextField()
    voting = models.ForeignKey(to=Votings, on_delete=models.CASCADE)
