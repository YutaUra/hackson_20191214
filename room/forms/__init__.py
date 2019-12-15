from django.forms import ModelForm

from room.models import Room


class RoomForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Room
        fields = (
            'name',
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

        )
