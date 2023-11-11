# from django.shortcuts import render

from django.http import HttpResponse

# from django.shortcuts import render

from part1.models import Url


def hello(request):
    urls = Url.objects.all()

    if urls:
        url_list = "<ul>"
        for url in urls:
            url_list += f"<li>{url.url_string}</li>"
        url_list += "</ul>"
    else:
        url_list = "No URLs available."

    return HttpResponse(
        f"""
        <h1>Hello Django !</h1>
        <p>Mes urls sont :</p>
        {url_list}
        """
    )
