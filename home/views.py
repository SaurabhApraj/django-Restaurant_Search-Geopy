from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from geopy.distance import great_circle

# Create your views here.
def home(request):
    return render(request, 'home.html')

def api(request):
    restraunt_objs = Restraunt.objects.all()

    pincode = request.GET.get('pincode')
    user_lat = None
    user_lon = None
    if pincode:
        geolocator = Nominatim(user_agent="geoapiExcercises")
        location = geolocator.geocode(int(pincode))
        user_lat = location.latitude
        user_lon = location.longitude

    payload = []
    for restraunt_obj in restraunt_objs:
        result = {}
        result['name'] = restraunt_obj.name
        result['image'] = restraunt_obj.image
        result['description'] = restraunt_obj.description
        result['pincode'] = restraunt_obj.pincode
        if pincode:
            result['distance'] = great_circle()
        payload.append(result)

    return JsonResponse(payload, safe=False)