from django.contrib import admin
from place.models import PlaceMeta


class PlaceMetaInline(admin.StackedInline):
    model = PlaceMeta


class PlaceAdmin(admin.ModelAdmin):
    inlines = [PlaceMetaInline, ]
    pass
