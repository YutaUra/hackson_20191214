from django.urls import reverse
from django.views.generic import DeleteView
from room.models import Room


class RoomDeleteView(DeleteView):
    model = Room
    template_name = 'room/delete.html'

    def get_success_url(self):
        return reverse('list')
