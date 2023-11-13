from django.http import HttpResponse
from django.shortcuts import render

from part1.models import Url


def url_list(request):
    urls = Url.objects.all()

    return render(request, "part1/url_list.html", {"urls": urls})


def url_detail(request, id):
    url = Url.objects.get(id=id)
    return render(request, "part1/url_detail.html", {"url": url})
