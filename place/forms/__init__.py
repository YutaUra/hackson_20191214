from django.forms import ModelForm, inlineformset_factory

from place.models import Place, PlaceMeta


class PlaceForm(ModelForm):
    class Meta:
        model = Place
        fields = (
            'name',
            'address',
        )


class PlaceMetaForm(ModelForm):
    class Meta:
        model = PlaceMeta
        fields = (
            'mood',
            'option',
        )


PlaceFormset = inlineformset_factory(
    Place, PlaceMeta, fields='__all__',
    extra=1, max_num=1, can_delete=False
)
