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
        + city + '&units=metric&appid=<Your Key>').read()
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

def textualdes(degree):
    if(degree>=337.5):
        return 'Northerly'
    if(degree>=292.5):
        return 'North Westerly'
    if(degree>=247.5):
        return 'Westerly'
    return 'Northerly'


def landing(request):
    return render(request,'main/landing.html')
