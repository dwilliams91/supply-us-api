from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from django.http import HttpResponseServerError
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from supplyusapi.models import ClassList, UserClass
from rest_framework.decorators import action


class ClassLists(ViewSet):
    def list(self, request):
        # get the current signed in user
        current_user=User.objects.get(auth_token=request.auth)
        if current_user.is_staff==True:
            all_class_lists=ClassList.objects.filter(user=current_user.id)
        else:
            all_class_lists=ClassList.objects.all()
            for classList in all_class_lists: 
                classList.joined=None
                try: 
                    user_classes=UserClass.objects.get(user=current_user, class_list=classList)
                    classList.joined=True
                except UserClass.DoesNotExist as ex:
                    classList.joined=False



        
        
        # send the class to the serializer
        serializer=ClassListSerializer(all_class_lists, many=True, context={'request':request})
        return Response(serializer.data)
    def create(self, request):
        # get current user
        current_user=User.objects.get(auth_token=request.auth)
        # create a new instance of a class and put in the data
        new_class=ClassList()
        new_class.class_name=request.data["class_name"]
        new_class.user=current_user
        # save the new class unless there is a validation error
        try:
            new_class.save()
            serializer=ClassListSerializer(new_class, many=False, context={'request':request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            class_to_delete=ClassList.objects.get(pk=pk)
            class_to_delete.delete()
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        except class_to_delete.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

class ClassListSerializer(serializers.ModelSerializer):
    class Meta:
        model= ClassList
        fields=('id','class_name', 'joined')