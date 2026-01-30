from django.db import models
from powerstrips.models import Child

# represents a device and its information
class DeviceTemplate(models.Model):
    type = models.CharField(max_length=50)
    model = models.CharField(max_length=50, unique=True)
    power = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.model} ({self.power}A)"


# represents a plugged-in device
class Device(models.Model):
    child_strip = models.ForeignKey(
        Child,
        related_name="devices",
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    template = models.ForeignKey(
        DeviceTemplate,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    slot = models.PositiveSmallIntegerField(null=True,blank=True)

    class Meta:
        unique_together = ('child_strip', 'slot')
        ordering = ['slot']

    def __str__(self):
        return f"{self.template.model} (Slot {self.slot})"
