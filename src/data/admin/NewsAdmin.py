from django.contrib import admin

from data import models
from data.admin import inlines

@admin.register(models.News)
class NewsAdmin(admin.ModelAdmin):
    list_display = [
        "title",
    ]

    fields = [
        "title",
        "text",
        "source",
    ]

    inlines = [
        inlines.TagInline,
    ]
