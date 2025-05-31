from django.db import models
from django.core.validators import MinLengthValidator,RegexValidator
from powerstrips.models import Parent

# Create your models here.
class Site(models.Model):
    #regex for site codes EX: NRT5
    site_code = models.CharField(max_length=4,primary_key=True)
    parent_power_strip = models.ManyToManyField(Parent,blank=True)

    def __str__(self):
        return self.site_code