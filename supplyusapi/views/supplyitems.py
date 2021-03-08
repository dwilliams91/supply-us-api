from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from django.http import HttpResponseServerError
from django.core.exceptions import ValidationError
from supplyusapi.models import SupplyItem

class SupplyItems(ViewSet):
    def list(self, request):

        all_supply_items=SupplyItem.objects.all()
        serializer=SupplyItemsSerializer(all_supply_items, many=True, context={'request':request})
        return Response(serializer.data)

class SupplyItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model=SupplyItem
        fields=('id', 'type', 'name')
        # depth=1