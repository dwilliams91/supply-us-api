from django.db import models
from django.contrib.auth.models import User


class UserClass(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="relateduser")
    class_list=models.ForeignKey("ClassList", on_delete=models.CASCADE, related_name="relatedclasses")