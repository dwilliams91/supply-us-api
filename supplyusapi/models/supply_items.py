from django.db import models

class SupplyItem(models.Model):
    name=models.CharField(max_length=200)
    type=models.ForeignKey("SupplyType", on_delete=models.CASCADE)
    shopping_link=models.CharField(max_length=200)
    imageURL=models.models.ImageField(("") upload_to=None, height_field=None, width_field=None, max_length=None)(max_length=250)
