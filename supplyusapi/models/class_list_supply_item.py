from django.db import models

class ClassListSupplyItem(models.Model):
    class_list=models.ForeignKey("ClassList", on_delete=models.CASCADE)
    supply_item=models.ForeignKey("SupplyItem", on_delete=models.CASCADE)
    number=models.IntegerField()
    description=models.CharField(max_length=250)
    package_type=models.ForeignKey("PackageType", on_delete=models.CASCADE)
