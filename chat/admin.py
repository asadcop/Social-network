from django.contrib import admin
from . import models
# Register your models here.

class MassageAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Massages,MassageAdmin)