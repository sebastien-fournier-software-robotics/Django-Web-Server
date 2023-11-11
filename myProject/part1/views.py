from django.http import HttpResponse
from django.shortcuts import render

from part1.models import Url


def hello(request):
    url_list = Url.objects.all()

    return render(request, "part1/hello.html", {"urls": url_list})
