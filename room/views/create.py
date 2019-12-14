from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView
from room.forms import RoomForm
from room.models import Room


class RoomCreateView(CreateView):
    model = Room
    form_class = RoomForm
    template_name = 'room/create.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return super().get(request, *args, **kwargs)
        return redirect('user:create')

    def get_success_url(self):
        return reverse('detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)
