import datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Place(models.Model):

    place_name = models.CharField(
        max_length=30,
        verbose_name=('place name')
    )

    class Meta():
        verbose_name=('place')
        verbose_name_plural=('places')

    def __str__(self):
        return self.place_name

class TypeOfStatus(models.Model):

    status_name = models.CharField(
        max_length=20,
        verbose_name=('status name')
    )

    class Meta():
        verbose_name=('type of status')
        verbose_name_plural=('type of status')

    def __str__(self):
        return self.status_name

class Status(models.Model):

    type_of_status = models.ForeignKey(
        TypeOfStatus,
        on_delete=models.PROTECT,
        
    )

    class Meta():
        verbose_name=('status')
        verbose_name_plural=('status')

    def __str__(self):
        return f"{self.pk}: {self.type_of_status.status_name}"

#Save the date, time, and user who made the change of status.
class StatusChangeLog(models.Model):
    status = models.ForeignKey(
        Status, 
        on_delete=models.CASCADE
    )
    modification_date = models.DateTimeField()
    modified_by = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        null=True
    )
    new_status_name = models.CharField(
        max_length=20
    )

    class Meta():
        verbose_name=('status change log')
        verbose_name_plural=('status change log')

    def __str__(self):
        return self.new_status_name

    def save(self, *args, **kwargs):
        if not self.modification_date:
            self.modification_date = timezone.now()
        self.new_status_name = self.status.status_name
        super().save(*args, **kwargs)

class Incidence(models.Model):

    comment = models.TextField(
        max_length=150,
        verbose_name=('comment')
    )
    
    place = models.ForeignKey(
        Place,
        on_delete=models.PROTECT,
        default=None
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.CASCADE,
        default=None
    )


    class Meta():
        verbose_name=('incidence')
        verbose_name_plural=('incidences')

    def __str__(self):
        return self.comment