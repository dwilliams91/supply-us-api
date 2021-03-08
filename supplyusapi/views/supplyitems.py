from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from rest_framework.decorators import action

from django.http import HttpResponseServerError
from django.core.exceptions import ValidationError
from supplyusapi.models import SupplyItem, SupplyType

class SupplyItems(ViewSet):
    def list(self, request):

        all_supply_items=SupplyItem.objects.all()
        serializer=SupplyItemsSerializer(all_supply_items, many=True, context={'request':request})
        return Response(serializer.data)

    @action(methods=['post'],detail=True)
    def typefilter(self,request, pk=None):
        # get the type that was selected
        selected_type=SupplyType.objects.get(pk=pk)
        # get the items from that type
        filtered_items=SupplyItem.objects.filter(type=selected_type)
        serializer=SupplyItemsSerializer(filtered_items, many=True, context={'request':request})
        return Response(serializer.data)


        
class SupplyItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model=SupplyItem
        fields=('id', 'type', 'name')
        # depth=1