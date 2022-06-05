from django import forms

class CoordinateForm(forms.Form):
    longitude = forms.FloatField(label='Longitude')
    latitude = forms.FloatField(label='Latitude')