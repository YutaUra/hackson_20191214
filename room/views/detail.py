from django.views.generic import DetailView
from room.models import Room


class RoomDetailView(DetailView):
    model = Room
    template_name = 'room/detail.html'
