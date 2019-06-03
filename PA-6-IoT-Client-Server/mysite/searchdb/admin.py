from django.contrib import admin

from .models import Sensorvalue

# Register your models here.

class SearchAdmin(admin.ModelAdmin):
    list_display = ("date", "cds",)


admin.site.register(Sensorvalue)
