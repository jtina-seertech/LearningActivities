# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from management.models import Assets, Status, AssetsBorrower
from management.serializers import AssetsSerializer, StatusSerializer, AssetsBorrowerSerializer

# Create your views here.
"""
    This is for specific assets
"""
@api_view(['GET', 'PUT', 'DELETE'])
def asset_detail(request, pk, format=None):

    try:
        assets = Assets.objects.get(pk=pk)
    except Assets.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = AssetsSerializer(assets)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AssetsSerializer(assets, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        assets.delete()
        return HttpResponse(status=204)

"""
    This is for asset list
"""
@api_view(['GET', 'POST'])
def assets_list(request, format=None):

    if request.method == 'GET':
        assets = Assets.objects.all()
        serializer = AssetsSerializer(assets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AssetsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

"""
    This is for status
"""
@api_view(['GET', 'POST'])
def status_list(request, format=None):

    if request.method == 'GET':
        assets = Status.objects.all()
        serializer = StatusSerializer(assets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = StatusSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

"""
    This is for assets borrowers
"""
@api_view(['GET', 'POST'])
def asset_borrower_list(request, format=None):

    if request.method == 'GET':
        assets = AssetsBorrower.objects.all()
        serializer = AssetsBorrowerSerializer(assets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AssetsBorrowerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)