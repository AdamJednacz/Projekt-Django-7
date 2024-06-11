from django.shortcuts import render,redirect,get_object_or_404

from .forms import PlaceForm,TripForm

from .models import Place,Trip,Favorite

def index(request):
  
    return render(request, 'www/index.html', {})
    

def add_place(request):
    if request.method == 'POST':
        form = PlaceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('places')
    else:
        form = PlaceForm()
    
    return render(request, 'www/add_place.html', {'form':form})


def places(request):
    places = Place.objects.all()
    return render(request, 'www/places.html', {'places':places})

def places_detail(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    trips = Trip.objects.filter(place=place)
    return render(request, 'www/places_detail.html', {'place': place, 'trips': trips})


def planing(request):
    if request.method == 'POST':
        form = TripForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('trips')
    else:
        form = TripForm()
    return render(request, 'www/planing.html', {'form':form})


def trips(request):
    trips = Trip.objects.all()
    if request.method == 'POST':
        trip_id = request.POST.get('trip')
        trip = get_object_or_404(Trip, id=trip_id)
       
        if not Favorite.objects.filter(trip=trip).exists():
            Favorite.objects.create(trip=trip)
        return redirect('favorite')
    else:
        return render(request, 'www/trips.html', {'trips': trips})




def favorite(request):
    favorite_trips = Favorite.objects.all()
    if request.method == 'POST':
        favorite_trip_id = request.POST.get('favorite_trip')
        favorite_trip = get_object_or_404(Favorite, id=favorite_trip_id)
        favorite_trip.delete()
        return redirect('favorite')
    else:
        return render(request, 'www/favorite.html', {'favorite_trips': favorite_trips})
    

