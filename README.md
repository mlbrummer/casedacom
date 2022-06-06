# Case Dacom
Simple API endpoint that publishes meteodata.

## Description

Simple API endpoint that can publish public available meteodata. It is used by a frontend webapplication to fill in longitude and latitude coordinates in the Netherlands, and return the place/location name, the amount of rain and the maximum temperature of the last 24 hours. 

Public meteo API URL that is used:
https://data.meteoserver.nl/api/liveweer_synop.php?lat=52.1052957&long=5.1806729&key=587ad5bdb8&selec t=1

This API is written in Django/Python (v3). 


## Getting Started

### Dependencies
* Python3
* Django 4.0.5
* djangorestframework 3.13.1
* python-decouple 3.6
* requests 2.27.1


### Installing/Executing program

* Fork project
* Create virtual env 
* Install dependencies
* In terminal go to casedacom_root, run: "python3 manage.py runserver" to run server, run "python3 manage.py test" to run unit tests.

```
python3 manage.py runserver
python3 manage.py test
```

* Go to http://localhost:8000


## Authors

Maaike Brummer
