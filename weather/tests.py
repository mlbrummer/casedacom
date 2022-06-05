from django.test import TestCase
from weather.views import WeatherData
from weather.views import Converter
from django.test.utils import override_settings 


# Test to see if getters work for three parameters in class WeatherData
class WeatherDataTestCase(TestCase):
    print("Testing WeatherDataTestCase")
    place = ""
    temp = 0.0
    rain = 0

    # Set values
    def setUp(self):
        WeatherData.setWeatherData(self, "Haren", 10.5, 3)

    # Check if values equals values from getters values
    def test_weatherdata(self):
        self.assertEqual(WeatherData.getPlace(self), "Haren")
        self.assertEqual(WeatherData.getMaxTemp(self), 10.5)
        self.assertEqual(WeatherData.getRain(self), 3)


# Unit test to check if message derives from invalid longitude and latitude values.
class ConverterTestCaseInvalidInputParams(TestCase):
    print("Testing ConverterTestCaseInvalidInputParams")
    fullJsonData = {}
    # Get data from meteoserver api with longitude and latitude values -1
    def setUp(self):
        Converter.getDataFromExternal(self, -1, -1)

    # Check if message is correct
    def test_getDataFromExternal(self):
        self.assertEqual(self.fullJsonData["message"], "Check input parameters")


# Override Meteo api private key
@override_settings(METEO_APP_KEY = 'testkey')
# Unit test to check the message with valide data, but a wrong meteo api key.
class ConverterTestCaseInvalidApiKey(TestCase):
    print("Testing ConverterTestCaseInvalidApiKey")
    fullJsonData = {}
    # Get data from meteoserver api with valid longitude and latitude values
    def setUp(self):
        Converter.getDataFromExternal(self, 6.60931, 53.17209)
    # Check if message is correct
    def test_getDataFromExternal(self):
        self.assertEqual(self.fullJsonData["message"], "Vraag eerst een API-key op, zie https://meteoserver.nl/account.php")

