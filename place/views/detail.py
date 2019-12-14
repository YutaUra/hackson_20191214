from django.views.generic import DetailView
from place.models import Place


class PlaceDetailView(DetailView):
    model = Place
    template_name = 'place/detail.html'
