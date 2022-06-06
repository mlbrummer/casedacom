# Case Dacom
Simple overview of use/purpose.

## Description

Simple API endpoint that can publish public available meteodata. It is used by a frontend webapplication to fill in longitude and latitude coordinates in the Netherlands, and return the amount of rain and maximum temperature of the last 24 hours. 

Public meteo API URL that is used:
https://data.meteoserver.nl/api/liveweer_synop.php?lat=52.1052957&long=5.1806729&key=587ad5bdb8&selec t=1

This API is written in Django/Python (v3). 


## Getting Started

### Dependencies
* Docker Desktop (Mac/Windows)
* Python3
* Django 4.0.5
* djangorestframework 3.13.1
* python-decouple 3.6
* requests 2.27.1


### Installing

* cd SollicitatieOpdrachtMaaikeBrummer
* docker-compose build

### Executing program

```
cd SollicitatieOpdrachtMaaikeBrummer
docker-compose up
```

* Go to http://localhost:8000

## Authors

Maaike Brummer (maaikebrummer96@gmail.com)