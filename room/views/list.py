from django.views.generic import ListView
from room.models import Room


class RoomListView(ListView):
    model = Room
    template_name = 'room/list.html'
