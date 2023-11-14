import requests
from bs4 import BeautifulSoup
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.response import Response

from part1.models import Url
from part1.serializers import UrlListSerializer

import logging


class UrlViewSet(viewsets.ModelViewSet):
    queryset = Url.objects.all()
    serializer_class = UrlListSerializer

    @action(detail=False, methods=["post"])
    def create_url(self, request):
        url = request.data.get("url")

        try:
            response = requests.get(url)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, "html.parser")
            title = soup.title.string
            images = [img["src"] for img in soup.find_all("img")]
            stylesheets = len(soup.find_all("link", rel="stylesheet"))

            domain_name = url.split("//")[-1].split("/")[0]
            protocol = url.split("://")[0]

            url_info_data = {
                "url_string": url,
                "domain_name": domain_name,
                "protocol": protocol,
                "title": title,
                "image": images,
                "stylesheets": stylesheets,
            }

            serializer = UrlListSerializer(data=url_info_data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(serializer.data)
        except requests.exceptions.RequestException as e:
            return Response({"error": str(e)}, status=400)
        except ValidationError as e:
            return Response({"error": str(e)}, status=400)
