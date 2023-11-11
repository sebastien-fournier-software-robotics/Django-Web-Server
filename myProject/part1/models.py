from django.db import models


class Url(models.Model):
    url_string = models.URLField()
    domain_name = models.CharField(max_length=255)
    protocol = models.CharField(max_length=5)
    title = models.CharField(max_length=255)
    image = models.JSONField(null=True, blank=True)
    stylesheets = models.PositiveIntegerField(default=0)
