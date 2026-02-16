from django.db import models


class DeviceTemplate(models.Model):
    device_type = models.CharField(max_length=50)
    model = models.CharField(max_length=50, unique=True)
    power = models.DecimalField(max_digits=6, decimal_places=2)  # Amps

    def __str__(self):
        return f"{self.model} ({self.power}A)"


class Device(models.Model):
    child = models.ForeignKey(
        "powerstrips.Child",
        related_name="devices",
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    template = models.ForeignKey(
        DeviceTemplate,
        on_delete=models.PROTECT
    )

    slot = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = ("child", "slot")
        ordering = ["slot"]

    def __str__(self):
        return f"{self.template.model} (Slot {self.slot})"
