"""Models of provider app."""
from django.db import models


class Provider(models.Model):
    """
    Model of provider, includes name, foundation year, status (active or not).
    """

    name = models.CharField(max_length=100, verbose_name="Naming")
    foundation_year = models.IntegerField(verbose_name="Year of foundation")
    is_active = models.BooleanField(verbose_name="Is active")

    def __str__(self):
        if self.is_active is False:
            return f"{self.name} | {self.foundation_year} | Inactive"
        return f"{self.name} | {self.foundation_year} | Active"
