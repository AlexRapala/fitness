from rest_framework import serializers
from lifting import models

class LogSerializer(serializers.ModelSerializer):
    """
    Ontop of default GET, POST, PUT, PATCH, and DELETE functionality:
        It will automatically generate a set of fields for you, based on the model.
        It will automatically generate validators for the serializer, such as unique_together validators.
        It includes simple default implementations of .create() and .update().
    """
    class Meta:
        model = models.Log
        fields = '__all__'


class LiftSerializer(serializers.ModelSerializer):
    """
    Ontop of default GET, POST, PUT, PATCH, and DELETE functionality:
        It will automatically generate a set of fields for you, based on the model.
        It will automatically generate validators for the serializer, such as unique_together validators.
        It includes simple default implementations of .create() and .update().
    """
    class Meta:
        model = models.Lift
        fields = '__all__'


class LogXLiftSerializer(serializers.ModelSerializer):
    """
    Ontop of default GET, POST, PUT, PATCH, and DELETE functionality:
        It will automatically generate a set of fields for you, based on the model.
        It will automatically generate validators for the serializer, such as unique_together validators.
        It includes simple default implementations of .create() and .update().
    """
    class Meta:
        model = models.LogXLift
        fields = '__all__'
        filterset_fields = ['log']
