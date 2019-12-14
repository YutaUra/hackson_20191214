from django.contrib.admin import site
from .admin import PlaceAdmin
from place.models import Place

site.register(Place, PlaceAdmin)
