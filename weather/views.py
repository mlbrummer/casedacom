from django.shortcuts import render
import requests
from django.conf import settings
from django.http import HttpResponse
from .forms import CoordinateForm
from django.contrib import messages

def home(request):
    weatherdata = {}
    if request.method == "GET":        
        coordinate_form = CoordinateForm(request.GET)

        if coordinate_form.is_valid():
            longitude = coordinate_form.cleaned_data["longitude"]
            latitude = coordinate_form.cleaned_data["latitude"]

            endpoint = 'https://data.meteoserver.nl/api/liveweer_synop.php?lat={latitude}&long={longitude}&key={key}'
            # Fill in lat, long and private key
            url = endpoint.format(latitude=latitude, longitude=longitude, key=settings.METEO_APP_KEY)
            # Get response
            response = requests.get(url)            
            if response.status_code == 200:
                try:
                    # Convert to json
                    weatherdata = response.json()
                except: #Errno Expecting value
                    weatherdata["message"] = "bad input parameter"
                print("weatherdata", weatherdata)
                weatherdata['success'] = True
            else:
                weatherdata['success'] = False

                if response.status_code == 400:
                    weatherdata["message"] = "bad input parameter"
                else:
                    weatherdata["message"] = "some error"

            weatherdata["longitude"] = longitude
            weatherdata["latitude"] = latitude


    # Return variables to weather_base html
    return render(request, "weather/weather_base.html", {
        "coordinate_form":coordinate_form, "weatherdata": weatherdata
        })




