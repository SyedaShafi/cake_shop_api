from rest_framework import serializers
from . import models

class UserPurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserPurchase
        fields = ['user', 'cake', 'cake_size']

class UserPurchaseSerializerWithAllFields(serializers.ModelSerializer):
    class Meta:
        model = models.UserPurchase
        fields = '__all__'


