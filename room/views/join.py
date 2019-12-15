"""detail -> joinで参加の処理"""
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404, redirect

from room.models import Room


class JoinView(TemplateView):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            room = get_object_or_404(Room, pk=kwargs.get('room_pk'))
            room.participant.add(request.user)
            room.owner.send_emai(f'{request.user}さんが{room}に参加しました！')
            room.save()
            return super().get(request, *args, **kwargs)
        return redirect('user:create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'object': get_object_or_404(Room, pk=kwargs.get('room_pk'))})
        return context
