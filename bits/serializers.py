from rest_framework import serializers
from .models import *


class ContentSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        return super().to_representation(instance)

    class Meta:
        model = Content
        fields = ['id', 'content', 'timestamp', 'marked', 'bits']


class GetBitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bits
        fields = "__all__"


class BitsSerializer(serializers.ModelSerializer):
    content = ContentSerializer(many=True)

    def to_representation(self, instance):
        return super().to_representation(instance)

    class Meta:
        model = Bits
        fields = "__all__"

    def create(self, validated_data):
        print('create started')
        contents_data = validated_data.pop('content')
        bits_instance = Bits.objects.create(**validated_data)

        for content_data in contents_data:
            Content.objects.create(bits=bits_instance, **content_data)

        return bits_instance

    def update(self, instance, validated_data):
        print('update started')
        instance.title = validated_data.get('title', instance.title)

        instance.save()
        return instance
