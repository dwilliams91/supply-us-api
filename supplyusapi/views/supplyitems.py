from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from rest_framework.decorators import action

from django.http import HttpResponseServerError
from django.core.exceptions import ValidationError
from supplyusapi.models import SupplyItem, SupplyType, ClassListSupplyItem, PackageType, ClassList

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

    @action(methods=['get', 'post'], detail=True)
    def classListSupplyItem(self, request, pk=None):
        if request.method=="GET":
            list_of_my_class_items=ClassListSupplyItem.objects.filter(class_list=pk)
            serializer=ClassListSupplyItemSerializer(list_of_my_class_items, many=True, context={'request':request})
            return Response(serializer.data)
        if request.method=="POST":

            new_item=ClassListSupplyItem()

            related_Class=ClassList.objects.get(pk=request.data["classListId"])
            related_supply_item=SupplyItem.objects.get(pk=request.data["supplyItemId"])
            related_PackageType=PackageType.objects.get(pk=request.data["packaging"])

            new_item.number=request.data["number"]
            new_item.class_list=related_Class
            new_item.supply_item=related_supply_item
            new_item.package_type= related_PackageType
            
            new_item.description=request.data["description"]
            serializer=ClassListSupplyItemSerializer(new_item, many=False, context={'request':request})
            return Response(status=status.HTTP_201_CREATED)
 

    

        
class SupplyItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model=SupplyItem
        fields=('id', 'type', 'name')
        # depth=1
class PackageTypeSerlializer(serializers.ModelSerializer):
    class Meta:
        model=PackageType
        fields=('id','type')

class ClassListSupplyItemSerializer(serializers.ModelSerializer):
    supply_item=SupplyItemsSerializer(many=False)
    package_type=PackageTypeSerlializer(many=False)
    class Meta:
        model= ClassListSupplyItem
        fields=('id', 'class_list', 'supply_item', 'number', 'description', 'package_type')
