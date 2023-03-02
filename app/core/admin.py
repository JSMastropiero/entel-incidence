from django.contrib import admin
from .models import Incidence, Place, TypeOfStatus, Status, StatusChangeLog

# Register your models here.

admin.site.register(Incidence)
admin.site.register(Place)
admin.site.register(TypeOfStatus)
admin.site.register(Status)
admin.site.register(StatusChangeLog)
