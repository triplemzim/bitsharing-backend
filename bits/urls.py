from django.urls import path, include
from rest_framework import routers
from .views import *

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'bits', BitsViewSet)
router.register(r'get_bits', BitsRetrieveViewSet, basename='get_bits')
router.register(r'contents', ContentViewSet, basename='contents')
router.register(r'unmarked_contents', UnmarkedContentViewSet, basename='unmarked_contents')

urlpatterns = [
    path('', include(router.urls)),
]
