from django.db import models

class SupplyItem(models.Model):
    name=models.CharField(max_length=200)
    type=models.ForeignKey("SupplyType", on_delete=models.CASCADE)
    shopping_link=models.CharField(max_length=500)
    imageURL=models.CharField(max_length=500)
