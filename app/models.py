from django.db import models


class Zepep(models.Model):
    name = models.CharField(max_length=128)
    user = models.CharField(max_length=128)
    friendship = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
