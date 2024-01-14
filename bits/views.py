from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.filters import SearchFilter

from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from .models import *


class BitsViewSet(ModelViewSet):
    queryset = Bits.objects.all()
    serializer_class = BitsSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ["code"]
    filterset_fields = ['code']


class BitsRetrieveViewSet(ReadOnlyModelViewSet):
    queryset = Bits.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['code']

    def get_serializer_class(self):
        return GetBitSerializer

    def get_queryset(self):
        code = self.request.query_params.get('code', None)
        if code:
            queryset = Bits.objects.filter(code=code)
            if not queryset.exists():
                # Create a new entry if the object with the specified code doesn't exist
                new_bit = Bits.objects.create(code=code)
                queryset = Bits.objects.filter(pk=new_bit.pk)
        else:
            queryset = Bits.objects.none()

        return queryset


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
