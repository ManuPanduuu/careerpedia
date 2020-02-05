
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import BachelorViewSet, IntermediateViewSet


router = routers.DefaultRouter()
router.register('bachelors', BachelorViewSet)
router.register('intermediate', IntermediateViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
