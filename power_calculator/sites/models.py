from django.db import models

# Create your models here.
class Site(models.Model):
    #regex for site codes EX: NRT5
    site_code = models.CharField(max_length=4,primary_key=True)
    parent_power_strip = models.ManyToManyField("powerstrips.parent",blank=True,related_name="sites")

    def __str__(self):
        return self.site_code