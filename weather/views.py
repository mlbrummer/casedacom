from django.shortcuts import render
import requests
from django.conf import settings
from django.http import HttpResponse

def home(request):
    # Define variables to output
    weatherdata = {}
    longitude = ""
    latitude = ""
    # Check if longitude and latitude are filled in.
    if 'longitude' in request.GET and 'latitude' in request.GET:
        longitude = request.GET['longitude']
        latitude = request.GET['latitude']
        # Create endpoint for meteoserver
        endpoint = 'https://data.meteoserver.nl/api/liveweer_synop.php?lat={latitude}&long={longitude}&key={key}'
        # Fill in lat, long and private key
        url = endpoint.format(latitude=latitude, longitude=longitude, key=settings.METEO_APP_KEY)
        # Get response
        response = requests.get(url)
        # Convert to json
        weatherdata = response.json()

    # Return variables to weather_base html
    return render(request, "weather/weather_base.html", {
        "weatherdata": weatherdata,
        "longitude":longitude,
        "latitude":latitude})
