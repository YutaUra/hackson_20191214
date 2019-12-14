from django.contrib.admin import site
from .admin import RoomAdmin
from room.models import Room

site.register(Room, RoomAdmin)
