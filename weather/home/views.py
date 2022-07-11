from django.shortcuts import render
import requests

# Create your views here.

def home(request):
    
    city = request.GET.get('city', "Jodhpur")
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=c4f5e41927b5417ee076bd9f9f218b6b'
    data=requests.get(url).json()

    payload = {
        'city' : data['name'],
        'weather' : data['weather'][0]['main'],
        'kelvin_temperature' : data['main']['temp'],
        'celcius_temperature' : int(data['main']['temp'] - 273),
        'pressure' : data['main']['pressure'],
        'humidity' : data['main']['humidity'],
        'description' : data['weather'][0]['description']
    }

    context = {'data' : payload}
    print(context)
    return render(request,'home.html' , context)