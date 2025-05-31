from django.db import models

# Create your models here.
class Child(models.Model):
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.location

class Parent(models.Model):
    name = models.CharField(max_length=20,primary_key=True)
    child_strips = models.ManyToManyField(Child)

    def __str__(self):
        return self.name

