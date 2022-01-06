from rest_framework import serializers

from news.models import *


class NewsReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = ('date', 'subject', 'content')
        read_only_fields = fields
