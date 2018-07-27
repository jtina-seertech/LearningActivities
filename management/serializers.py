from rest_framework import serializers
import datetime
from management.models import Assets, Status, AssetsBorrower


class AssetsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False, allow_blank=True, max_length=100)
    asset_type = serializers.CharField(required=False, allow_blank=True, max_length=100)

    def create(self, validated_data):
        return Assets.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.asset_type = validated_data.get('asset_type', instance.asset_type)
        if self.is_valid():
            instance.save()
        return instance

class StatusSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False, allow_blank=True, max_length=100)

    def create(self, validated_data):
        return Status.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        return instance

class AssetsBorrowerSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    date = serializers.DateTimeField(initial=datetime.date.today)
    user_id = serializers.IntegerField(read_only=True)
    asset_id = serializers.IntegerField(read_only=True)
    status_id = serializers.IntegerField(read_only=True)

    def create(self, validated_data):
        return AssetsBorrower.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('title', instance.name)
        return instance