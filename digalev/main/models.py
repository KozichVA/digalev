from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=24, unique=True, blank=False, null=False)
    description = models.
# Create your models here.
