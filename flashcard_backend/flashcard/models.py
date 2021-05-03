from django.db import models


# Create your models here.
class Flashcard(models.Model):
    flashcard_term = models.CharField(max_length=50, null=True)
    flashcard_definition = models.CharField(max_length=50, null=True)