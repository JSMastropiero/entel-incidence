from datetime import timezone
from django.db import models


# Create your models here.

class Incidence(models.Model):

    comment = models.TextField(
        max_length=150,
        verbose_name=('comment')
    )


class Place(models.Model):

    place_name = models.CharField(
        max_length=30,
        verbose_name=('place name')
    )


class TypeOfStatus(models.Model):

    status_name = models.CharField(
        max_length=20,
        verbose_name=('status name')
    )


class Status(models.Model):

    type_of_status = models.ForeignKey(
        TypeOfStatus,
        on_delete=models.PROTECT,
        
    )


#Save the date, time, and user who made the change of status.
class StatusChangeLog(models.Model):
    status = models.ForeignKey(
        Status, 
        on_delete=models.CASCADE
    )
    modification_date = models.DateTimeField(
        default=timezone.now
    )
    modified_by = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        null=True
    )
    new_status_name = models.CharField(
        max_length=20
    )

    def save(self, *args, **kwargs):
        self.new_status_name = self.status.status_name
        super().save(*args, **kwargs)