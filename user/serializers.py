from rest_framework import serializers
from . import models

class ProfileSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField(read_only=True)
    class Meta:
        model = models.ProfileModel
        fields = '__all__'
