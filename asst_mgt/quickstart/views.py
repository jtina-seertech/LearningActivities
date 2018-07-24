# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models import User, Group
from management.models import Assets, Status, AssetsBorrower
from rest_framework import viewsets
from asst_mgt.quickstart.serializers import UserSerializer, GroupSerializer,\
    AssetsSerializer, StatusSerializer, BorrowerSerializer

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class AssetsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows assets to be viewed or edited.
    """
    queryset = Assets.objects.all()
    serializer_class = AssetsSerializer

class StatusViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows status to be viewed or edited.
    """
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

class BorrowerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows borrower to be viewed or edited.
    """
    queryset = AssetsBorrower.objects.all()
    serializer_class = BorrowerSerializer

