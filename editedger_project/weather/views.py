import requests
from django.shortcuts import render
from .models import City

# Create your views here.
def weather(request):
	url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=e357f3a75f4a8d5c96ccb0742cccdc27"
	cities = City.objects.all()
	cities_data = []

	for city in cities:

		r = requests.get(url.format(city)).json()

		city_data = {
			'name' : city.name,
			'temperature' : r['main']['temp'],
			'description' : r['weather'][0]['description'],
			'icon' : r['weather'][0]['icon'],
		}

		cities_data.append(city_data)

	context = {'cities': cities_data}
	return render(request, 'weather.html', context)