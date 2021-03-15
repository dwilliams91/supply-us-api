from django.db import models
from django.contrib.auth.models import User


class ClassList(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    class_name=models.CharField(max_length=50)

    @property
    def joined(self):
        return self.__joined

    @joined.setter 
    def joined(self, value):
        self.__joined = value