from rest_framework import serializers

class ProfileSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField(read_only=True)
    class Meta:
        model = ProfileModel
        fields = '__all__'
