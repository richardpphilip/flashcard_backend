from django.db import models


# Create your models here.
class Collection(models.Model):
    collection_name = models.CharField(max_length=50, null=True)
