from rest_framework import serializers
from .models import *


class ContentSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        return super().to_representation(instance)

    class Meta:
        model = Content
        fields = "__all__"


class BitsSerializer(serializers.ModelSerializer):
    # contents = ContentSerializer(many=True, source='content')

    def to_representation(self, instance):
        return super().to_representation(instance)

    class Meta:
        model = Bits
        fields = "__all__"
