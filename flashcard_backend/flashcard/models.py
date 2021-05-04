from django.db import models


# Create your models here.
class Flashcard(models.Model):
    collection_name = models.ForeignKey('collection.Collection', null=True, on_delete=models.CASCADE)
    flashcard_term = models.CharField(max_length=50, null=True)
    flashcard_definition = models.CharField(max_length=50, null=True)
