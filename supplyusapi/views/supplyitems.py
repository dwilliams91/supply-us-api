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
    def create(self, request):
        created_item=SupplyItem()

        supply_type=SupplyType.objects.get(pk=request.data["supplyType"])
        
        created_item.name=request.data["name"]
        created_item.type=supply_type

        try:
            created_item.save()
            package_types=request.data["package_types"]
            for item in package_types:
                new_package_type=PackageType()
                new_package_type.supply_item=created_item
                new_package_type.type=item["type"]
                new_package_type.is_active_type=1
                new_package_type.save()
            serializer=SupplyItemsSerializer(created_item, many=False, context={'request':request})
            return Response(serializer.data)

        except SupplyType.DoesNotExist as ex:
                return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        supply_item=SupplyItem.objects.get(pk=pk)
        supply_type=SupplyType.objects.get(pk=request.data["supplyType"])
        supply_item.name=request.data["name"]
        supply_item.type=supply_type
        supply_item.save()
        
        # update packaging
        previous_packages=PackageType.objects.filter(supply_item=supply_item)
        updated_package_types=request.data["package_types"]
        
        # compare the lengths to find out if a package type was added or deleted
        # if previous is less than updated, an item was added
        print("does this hit 1")
        if len(list(previous_packages))<len(updated_package_types):
            print("does this hit 2")
            for item in updated_package_types:   
                package_found=previous_packages.filter(pk=item["id"])
                print(package_found)
                if len(list(package_found))==0:
                    # if the item doesn't exist, add it. 
                    print("does this hit 3")
                    new_package_type=PackageType()
                    new_package_type.supply_item=supply_item
                    new_package_type.type=item["type"]
                    new_package_type.is_active_type=1
                    new_package_type.save()
        # else:
        #     for item in updated_package_types:
        #         try:
        #             package_found=PackageType.objects.get(pk=item["id"])
        #         except PackageType.DoesNotExist as ex:
        #             # if the item doesn't exist, add it. 
        #             new_package_type=PackageType()
        #             new_package_type.supply_item=supply_item
        #             new_package_type.type=item["type"]
        #             new_package_type.is_active_type=1
        #             new_package_type.save()
        



            

        serializer=SupplyItemsSerializer(supply_item, many=False, context={'request':request})
        return Response(serializer.data)
        
    @action(methods=['post'],detail=True)
    def typefilter(self,request, pk=None):
        # get the type that was selected
        selected_type=SupplyType.objects.get(pk=pk)
        # get the items from that type
        filtered_items=SupplyItem.objects.filter(type=selected_type)
        serializer=SupplyItemsSerializer(filtered_items, many=True, context={'request':request})
        return Response(serializer.data)

    @action(methods=['post'],detail=False)
    def searchfilter(self,request,pk=None):

        filtered_items=SupplyItem.objects.filter(name__startswith=request.data["searchTerm"])
        serializer=SupplyItemsSerializer(filtered_items, many=True, context={'request':request})
        return Response(serializer.data)

    @action(methods=['get'], detail=True)
    def getSupplyLists(self, request, pk=None):
        if request.method=="GET":
            list_of_my_class_items=ClassListSupplyItem.objects.filter(class_list=pk)
            serializer=ClassListSupplyItemSerializer(list_of_my_class_items, many=True, context={'request':request})
            return Response(serializer.data)

    @action(methods=['post', 'delete'], detail=False)
    def manageSupplyLists(self, request, pk=None):
        if request.method=="POST":
            try:
                new_item=ClassListSupplyItem()

                related_Class=ClassList.objects.get(pk=request.data["classListId"])
                related_supply_item=SupplyItem.objects.get(pk=request.data["supplyItemId"])
                related_PackageType=PackageType.objects.get(pk=request.data["packaging"])

                if related_supply_item.id !=related_PackageType.supply_item_id:
                    print("doesn't match")
                    return Response({"reason": "supply item and package type don't align"}, status=status.HTTP_400_BAD_REQUEST)
                
                new_item.class_list=related_Class
                new_item.supply_item=related_supply_item
                new_item.package_type= related_PackageType
                new_item.number=request.data["number"]
                new_item.description=request.data["description"]

                new_item.save()
                serializer=ClassListSupplyItemSerializer(new_item, many=False, context={'request':request})

                
            except ClassList.DoesNotExist as ex:
                return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
            except SupplyItem.DoesNotExist as ex:
                return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
            except PackageType.DoesNotExist as ex:
                return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        if request.method=="DELETE":
            try:
                item_to_delete=ClassListSupplyItem.objects.get(pk=request.data['classListSupplyItemId'])
                item_to_delete.delete()

                return Response({}, status=status.HTTP_204_NO_CONTENT)

            except SupplyItem.DoesNotExist as ex:
                return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)


        
class SupplyItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model=SupplyItem
        fields=('id', 'type', 'name')
        # depth=1
class PackageTypeSerlializer(serializers.ModelSerializer):
    class Meta:
        model=PackageType
        fields=('id','type', "is_active_type")

class ClassListSupplyItemSerializer(serializers.ModelSerializer):
    supply_item=SupplyItemsSerializer(many=False)
    package_type=PackageTypeSerlializer(many=False)
    class Meta:
        model= ClassListSupplyItem
        fields=('id', 'class_list', 'supply_item', 'number', 'description', 'package_type')
