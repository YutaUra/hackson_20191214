from django.urls import reverse
from django.views.generic import UpdateView
from room.forms import RoomForm
from room.models import Room


class RoomUpdateView(UpdateView):
    model = Room
    form_class = RoomForm
    template_name = 'room/update.html'

    def get_success_url(self):
        return reverse('detail', kwargs={'pk': self.object.pk})
