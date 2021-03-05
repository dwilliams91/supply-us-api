from django.db import models

class SupplyType(models.Model):
    type=models.CharField(max_length=50)