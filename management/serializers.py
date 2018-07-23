from rest_framework import serializers
from management.models import Assets


class AssetsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False, allow_blank=True, max_length=100)
    asset_type = serializers.CharField(required=False, allow_blank=True, max_length=100)

    def create(self, validated_data):
        return Assets.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('title', instance.name)
        instance.asset_type = validated_data.get('code', instance.asset_type)
        return instance