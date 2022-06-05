from django import forms

class CoordinateForm(forms.Form):
    longitude = forms.FloatField(label='Longitude') # 6.60931
    latitude = forms.FloatField(label='Latitude') # 53.17209