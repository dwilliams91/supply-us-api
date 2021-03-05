from django.db import models
from django.contrib.auth.models import User


class ClassList(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    class_name=models.CharField(max_length=50)