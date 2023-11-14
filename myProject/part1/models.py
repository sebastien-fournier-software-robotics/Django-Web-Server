from django.db import models
from django.utils.translation import gettext_lazy as _


class protocol(models.TextChoices):
    HTTP = "http", "HTTP"
    HTTPS = "https", "HTTPS"


class Url(models.Model):
    url_string = models.URLField()
    domain_name = models.CharField(max_length=255)
    protocol = models.fields.CharField(choices=protocol.choices, max_length=5)
    title = models.CharField(max_length=255)
    image = models.JSONField(null=True, blank=True, default=list)
    stylesheets = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.url_string}"
