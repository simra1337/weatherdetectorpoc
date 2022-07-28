import string
from django.shortcuts import render
import os
import json
import urllib
from dotenv import load_dotenv

load_dotenv()

def home(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        api = 'https://api.weatherapi.com/v1/current.json?key='+os.getenv('API_KEY')+'&q='+city+'&aqi=no'
        json_data = urllib.request.urlopen(api).read()
        jsonResponse = json.loads(json_data.decode('utf-8'))
        temp = jsonResponse['current']['temp_c']
        return render(request, 'home.html', {'temp' : temp})
    else:
        city = ''
    return render(request, 'home.html', {'city': city})