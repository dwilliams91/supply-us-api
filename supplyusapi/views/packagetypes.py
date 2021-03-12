from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from django.http import HttpResponseServerError
from django.core.exceptions import ValidationError
from supplyusapi.models import PackageType, SupplyItem
from rest_framework.decorators import action

class PackageTypes(ViewSet):
    @action(methods=['GET'],detail=True)
    def getRelatedPackageTypes(self,request, pk=None):
        
        selected_item=SupplyItem.objects.get(pk=pk)
        try:
            related_packages=PackageType.objects.filter(supply_item=selected_item)   
            serializer=PackageTypeSerlializer(related_packages, many=True, context={'request',request})
            return Response(serializer.data)
        except selected_item.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
class PackageTypeSerlializer(serializers.ModelSerializer):
    class Meta:
        model=PackageType
        fields=('id','type', "supply_item")