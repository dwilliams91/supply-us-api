from django.db import models

class UserClass(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    class_list=models.ForeignKey("ClassList", on_delete=models.CASCADE)