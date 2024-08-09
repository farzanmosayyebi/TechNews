from django.contrib import admin

from data import models

class TagInline(admin.TabularInline):
    model = models.News.tags.through
    