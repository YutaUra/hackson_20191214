from django.views.generic import ListView
from room.models import Room


class RoomListView(ListView):
    model = Room
    queryset = Room.objects.filter(is_open=True)
    template_name = 'room/list.html'
