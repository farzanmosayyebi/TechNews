from django.contrib import admin

from data import models

@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = [
        "title"
    ]

    fields = [
        "title"
    ]