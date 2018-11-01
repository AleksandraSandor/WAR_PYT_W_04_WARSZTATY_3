
from django.forms import ModelForm, HiddenInput
from .models import Sala, Reservation
from django import forms

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

class SearchForm(forms.Form):
    name = forms.CharField(max_length=64, required=False)
    capacity = forms.IntegerField(required=False, label='Minimalna pojemność sali')
    date = forms.DateField(required=False)
    is_projector = forms.BooleanField(required=False)