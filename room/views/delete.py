from django.urls import reverse
from django.views.generic import TemplateView
from room.models import Room


class RoomDeleteView(TemplateView):
    model = Room
    template_name = 'room/delete.html'

    def get(self, request, *args, **kwargs):
        room = Room.objects.get(pk=kwargs.get('pk'))
        if request.user == room.owner:
            room.delete()
            return reverse('room:list')
        return super().get(request, *args, **kwargs)
