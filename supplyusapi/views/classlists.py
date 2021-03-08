from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from django.http import HttpResponseServerError
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class ClassLists(ViewSet):
    def list(self, request):
        author= User.objects.get(user=request.auth.user)