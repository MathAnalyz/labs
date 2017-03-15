from django import forms
from .models import Plant


class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = ('rus_name', 'lat_name', 'info', 'sec_measures', 'status', 'division', 'reservations', )