from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.

class Incidence(models.Model):


    comment = models.TextField(
        max_length=150,
        verbose_name=('comment')
    )

