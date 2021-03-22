from django.contrib import admin
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from django.http import HttpResponseServerError
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from supplyusapi.models import ClassList, UserClass
from rest_framework.decorators import action

class Admins(ViewSet):

    @action(methods=['Get'],detail=True)
    def getPendingTeachers(self,request,pk=None):
        current_user=User.objects.get(auth_token=request.auth)
        if current_user.is_superuser==True:
            pending_teachers=User.objects.get(is_active=False)
        serializer=UserSerlializer(pending_teachers, many=True, context={'request':request})
        return Response(serializer.data)
class UserSerlializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('email')
