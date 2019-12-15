from django.forms import ModelForm

from room.models import Room


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = (
            'name',
            'place',
            'object_nature',
            'object_bath',
            'object_gourmet',
            'object_historic',
            'object_shopping',
            'object_zoo_aquarium',
            'object_art',
            'object_sport',
            'object_other',
            'object_any',
            'mood',
            'option',
        )
