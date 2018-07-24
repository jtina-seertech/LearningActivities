from django.contrib.auth.models import User, Group
from management.models import Assets, Status, AssetsBorrower
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'first_name','last_name')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class AssetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assets
        fields = ('id', 'name', 'asset_type')

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ('id', 'name')

class BorrowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetsBorrower
        fields = ('id', 'date', 'user_id', 'asset_id', 'status_id')
