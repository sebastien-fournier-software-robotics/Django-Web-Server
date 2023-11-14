from rest_framework import serializers

from part1.models import Url


class UrlListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = "__all__"
