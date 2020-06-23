from rest_framework import viewsets
from lifting import serializers
from lifting import models
from django.http import HttpResponse

class LogViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.LogSerializer

    def get_queryset(self):
        return models.Log.objects.filter(owner=self.request.user)

class LiftViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.LiftSerializer

    def get_queryset(self):
        return models.Lift.objects.all()

class LogXLiftViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.LogXLiftSerializer

    def get_queryset(self):
        return models.LogXLift.objects.filter(log__owner=self.request.user)