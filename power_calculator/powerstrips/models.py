from django.db import models

class Child(models.Model):
    location = models.CharField(max_length=50)

    # NEW: total amperage helper
    def total_power(self):
        return sum(
            device.template.power
            for device in self.devices.all()
            if device.template
        )

    def __str__(self):
        return self.location


class Parent(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    child_strips = models.ManyToManyField(Child)

    def __str__(self):
        return self.name
