from django.urls import reverse
from django.views.generic import DeleteView
from place.models import Place


class PlaceDeleteView(DeleteView):
    model = Place
    template_name = 'place/delete.html'

    def get_success_url(self):
        return reverse('list')
