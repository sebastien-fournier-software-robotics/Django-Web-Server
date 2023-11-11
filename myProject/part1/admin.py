from django.contrib import admin
from part1.models import Url

# login: seb


class UrlAdmin(admin.ModelAdmin):
    list_display = ("url_string", "domain_name", "title")


admin.site.register(Url, UrlAdmin)
