from rest_framework import serializers
from .models import DatacollectionModel

class MyModelSerializer(serializers.ModelSerializer):
    """
    Serializer for the DatacollectionModel model.

    Serializes DatacollectionModel instances into JSON representations and vice versa.
    """

    class Meta:
        """
        Meta class for defining serializer behavior.
        """
        model = DatacollectionModel
        fields = ["id", "pulse_type", "tongue_type"]
