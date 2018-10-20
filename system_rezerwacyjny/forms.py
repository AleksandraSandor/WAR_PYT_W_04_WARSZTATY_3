from django import forms

from .models import Sala


class PostForm(forms.ModelForm):
    class Meta:
        model = Sala
        fields = ('name', 'capacity', 'is_projector',)

