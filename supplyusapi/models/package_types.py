from django.db import models

class PackageType(models.Model):
    supply_item=models.ForeignKey("SupplyItem", on_delete=models.CASCADE)
    type=models.CharField(max_length=50)