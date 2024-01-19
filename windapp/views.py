from django.shortcuts import render
import urllib.request
import json

# Create your views here.
def main(request):
    if request.method == 'POST':
        citycountry = request.POST['city']
        city, country= citycountry.split(',')
        city = city.replace(" ", "+")
        source = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q=' 
        + city + '&units=metric&appid=5e9e52d2d35442f9762b296ff8bac9f7').read()
        alldata = json.loads(source)

        data = {
            "country_code": str(alldata['sys']['country']),
            "coordinate": str(alldata['coord']['lon']) + ', '
            + str(alldata['coord']['lat']),

            "temp": str(alldata['main']['temp']) + ' °C',
            "pressure": str(alldata['main']['pressure']),
            "humidity": str(alldata['main']['humidity']),
            'main': str(alldata['weather'][0]['main']),
            'description': str(alldata['weather'][0]['description']),
            'icon': alldata['weather'][0]['icon'],
            'speed': alldata['wind']['speed'],
            'degree': alldata['wind']['deg'],
            'name': str(alldata['name']),
            
        }
        print(data)
    else:
        data = {}

    return render(request, "main/index.html", data)

def landing(request):
    return render(request,'main/landing.html')
