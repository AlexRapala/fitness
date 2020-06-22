from rest_framework import viewsets
from lifting import serializers
from lifting import models
from django.http import HttpResponse

class LogViewSet(viewsets.ModelViewSet):
    queryset = models.Log.objects.all()
    serializer_class = serializers.LogSerializer


class LiftViewSet(viewsets.ModelViewSet):
    queryset = models.Log.objects.all()
    serializer_class = serializers.LiftSerializer


class LogXLiftViewSet(viewsets.ModelViewSet):
    queryset = models.LogXLift.objects.all()
    serializer_class = serializers.LogXLiftSerializer