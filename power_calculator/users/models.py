from django.db import models
from sites.models import Site
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    sites = models.ManyToManyField(Site,blank=True)

    def __str__(self):
        return self.user.username
