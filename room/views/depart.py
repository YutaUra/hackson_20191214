"""detail -> departで出発の処理(マップの表示)"""
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from room.models import Room


class DepartView(TemplateView):
    template_name = 'room/depart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        room = get_object_or_404(Room, pk=kwargs.get('pk'))
        context.update({'room': room})
        context.update({'object': room})

        return context
