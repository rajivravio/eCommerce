from django.contrib import admin

from .models import Item

@admin.register(Item)
class adminU(admin.ModelAdmin):
    pass