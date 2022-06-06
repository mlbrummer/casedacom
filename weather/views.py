from django.shortcuts import render
import requests
from django.conf import settings
from django.http import HttpResponse
from .forms import CoordinateForm
from django.contrib import messages
from django.views.generic import ListView

# Class to save weatherdata variables by getters and setters.
class WeatherData():
    place = ""
    temp = 0.0
    rain = 0
    message = ""

    def getRain(self):
        return self.rain

    def getMaxTemp(self):
        return self.temp

    def getPlace(self):
        return self.place
    
    def getMessage(self):
        return self.message

    def setWeatherData(self, place, temp, rain):
        self.place = place
        self.temp = temp
        self.rain = rain
    
    def setMessage(self, message):
        self.message = message


# Class to convert longitude and latitude floats into weatherdata variables.
class Converter(ListView):
    fullJsonData = {}

    # Function to call Meteoserver api with longitude and latitude values, save response and messages
    def getDataFromExternal(self, longitude, latitude):
        # Define endpoint
        endpoint = 'https://data.meteoserver.nl/api/liveweer_synop.php?lat={latitude}&long={longitude}&key={key}'
        # Fill in latitude, longitude and private api key
        url = endpoint.format(latitude=latitude, longitude=longitude, key=settings.METEO_APP_KEY)
        # Get response
        response = requests.get(url)
        # Check for response statuscodes 200 and 400.
        if response.status_code == 200:
            try:
                # Convert to json
                self.fullJsonData = response.json()
                # Set message to empty
                self.fullJsonData["message"] = ""
                # Check if api key error is present in fullJsonData, if so, set as message
                if "api_key_invalid" in self.fullJsonData:
                    self.fullJsonData["message"] = self.fullJsonData["api_key_invalid"]
            except: #Errno Expecting value
                self.fullJsonData = {}
                self.fullJsonData["message"] = "Check input parameters"
        elif response.status_code == 400:
            self.fullJsonData["message"] =  "Check input parameters"
        
    # Function to save data derived from getDataFromExternal to WeatherData class
    def convert(self, weatherdata):
        # Save message to weatherdata message
        weatherdata.setMessage(self.fullJsonData["message"])
        # Check if there was no message, and "liveweer" is available in fullJasonData
        if len(weatherdata.getMessage()) == 0 and "liveweer" in self.fullJsonData:
            weatherdata.setWeatherData(self.fullJsonData["liveweer"][0]["plaats"], self.fullJsonData["liveweer"][0]["temp_24"], self.fullJsonData["liveweer"][0]["regen_24"])


def index(request):
    # Initialize Converter and WeatherData classes
    converter = Converter()
    weatherdata = WeatherData()
    coordinates_filled_in = False
    
    # Check if request method is post, get data
    if request.method == "POST":       
        # Get coordinate_form and check if form values are valid
        coordinate_form = CoordinateForm(request.POST)
        #coordinate_form = CoordinateForm()
        if coordinate_form.is_valid():
            # Get longitude and latitude values from coordinate form
            longitude = coordinate_form.cleaned_data["longitude"]
            latitude = coordinate_form.cleaned_data["latitude"]
            coordinates_filled_in = True
            # Call getDataFromExternal with variables longitude and latitude
            converter.getDataFromExternal(longitude, latitude)
            # Save outcome to weatherdata
            converter.convert(weatherdata)
    # Check if request method is get, create unbound coordinate form
    else:
        coordinate_form = CoordinateForm() 

    # Return variables to weather_base html
    return render(request, "weather/weather_base.html", {
        "coordinate_form":coordinate_form, 
        "coordinates":coordinates_filled_in,
        "place":weatherdata.getPlace(), 
        "max_temp":weatherdata.getMaxTemp(), 
        "rain":weatherdata.getRain(), 
        "message":weatherdata.getMessage()
        })