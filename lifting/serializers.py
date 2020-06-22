from rest_framework import serializers
from lifting import models

class LogSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Log
        fields = '__all__'


class LiftSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Lift
        fields = '__all__'


class LogXLiftSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.LogXLift
        fields = '__all__'