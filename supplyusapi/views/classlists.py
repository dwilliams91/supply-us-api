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
        # get the current signed in user
        current_user=User.objects.get(auth_token=request.auth)
        # get only the classes created by the user
        all_class_lists=ClassList.objects.filter(user=current_user.id)
        # send the class to the serializer
        serializer=ClassListSerializer(all_class_lists, many=True, context={'request':request})
        return Response(serializer.data)
        
class ClassListSerializer(serializers.ModelSerializer):
    class Meta:
        model= ClassList
        fields=('id','class_name')