from django.db import models


class Child(models.Model):
    location = models.CharField(max_length=50)

    def total_power(self):
        return sum(
            device.template.power
            for device in self.devices.all()
            if device.template
        )

    def __str__(self):
        return self.location


class Parent(models.Model):
    site = models.ForeignKey(
        "sites.Site",
        on_delete=models.CASCADE,
        related_name="parent_strips"
    )

    name = models.CharField(max_length=20)

    child_strips = models.ManyToManyField(
        Child,
        related_name="parents",
        blank=True
    )

    def __str__(self):
        return f"{self.site.site_code} | {self.name}"
