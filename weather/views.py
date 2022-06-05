from django.shortcuts import render
import requests
from django.conf import settings
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Live weather API</h1>")

