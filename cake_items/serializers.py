from rest_framework import serializers
from . import models

class CakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CakeModel
        fields = '__all__'
