from django.db import models
from powerstrips.models import Child

# Create your models here.
class Device(models.Model):

    type = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    power = models.DecimalField(max_digits=5,decimal_places=2)
    child_strip = models.ForeignKey(Child,on_delete=models.CASCADE)

    def __str__(self):
        return self.model