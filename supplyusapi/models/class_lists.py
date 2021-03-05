from django.db import models

class ClassList(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    class_name=models.CharField(max_length=50)