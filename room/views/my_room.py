from django.urls import reverse
from django.views.generic import RedirectView


class MyRoomView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        user = self.request.user
        room = user.current_room()
        if room:
            return reverse('room:detail', kwargs={'pk':room.pk})
        return reverse('room:list')
