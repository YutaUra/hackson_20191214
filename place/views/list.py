from django.views.generic import ListView
from place.models import Place


class PlaceListView(ListView):
    model = Place
    template_name = 'place/list.html'
