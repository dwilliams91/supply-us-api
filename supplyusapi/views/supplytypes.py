from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from django.http import HttpResponseServerError
from django.core.exceptions import ValidationError
from supplyusapi.models import SupplyType

class SupplyTypes(ViewSet):
    def list(self, request):
        
        all_supply_types=SupplyType.objects.all()
        serializer=SupplyTypeSerializer(all_supply_types, many=True, context={'request':request})
        return Response(serializer.data)

class SupplyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=SupplyType
        fields=('id', 'type')