from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from django.http import HttpResponseServerError
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from supplyusapi.models import ClassList


class ClassLists(ViewSet):
    def list(self, request):
        classlists=ClassList.objects.all()
        print(classlists)
        serializer=ClassListSerializer(classlists, many=True, context={'request':request})
        return Response(serializer.data)
        
class ClassListSerializer(serializers.ModelSerializer):
    class Meta:
        model= ClassList
        fields=('id','class_name')