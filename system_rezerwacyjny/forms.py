
from django.forms import ModelForm, HiddenInput
from .models import Sala, Reservation


class PostForm(ModelForm):
    class Meta:
        model = Sala
        fields = ('name', 'capacity', 'is_projector',)


class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ('date', 'id_sali', 'note')
        widgets = {
            'id_sali': HiddenInput()
        }

