import random
from django.shortcuts import render
from myapp.models import Scenery, City

# Create your views here.
def index(request):
	context = {}
	cities = City.objects.all()
	context['cities'] = cities
	return render(request, 'index.html', context)

def wander(request):
	context = {}
	cityId = request.GET.get("city")
	city = City.objects.get(id=cityId)
	sceneries = Scenery.objects.filter(city_id=cityId)
	context['city'] = city
	context['sceneries'] = sceneries
	styleN = random.randint(1, 4)
	context['styleN'] = styleN
	return render(request, 'landing.html', context)