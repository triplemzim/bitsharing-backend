from rest_framework.viewsets import ModelViewSet, mixins, GenericViewSet
from rest_framework.filters import SearchFilter
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from .models import *


class BitsViewSet(ModelViewSet):
    queryset = Bits.objects.all()
    serializer_class = BitsSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ["username", "code"]
    filterset_fields = ['username', 'code']


class ContentViewSet(ModelViewSet):
    queryset = Content.objects.all().order_by('-id')
    serializer_class = ContentSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['content']
    filterset_fields = ['bits']


class UnmarkedContentViewSet(ModelViewSet):
    queryset = Content.objects.filter(marked=False).order_by('-id')
    serializer_class = ContentSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['content']
    filterset_fields = ['bits']
