from django.urls import reverse
from django.views.generic import UpdateView
from place.forms import PlaceForm
from place.models import Place


class PlaceUpdateView(UpdateView):
    model = Place
    form_class = PlaceForm
    template_name = 'place/update.html'

    def get_success_url(self):
        return reverse('detail', kwargs={'pk': self.object.pk})
