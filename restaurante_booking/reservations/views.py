from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from .models import Restaurant, Reservation
from .forms import ReservationForm

def restaurant_list(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'reservations/restaurant_list.html', {'restaurants': restaurants})

def make_reservation(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.restaurant = restaurant
            reservation.save()
            return redirect('reservation_success')
    else:
        form = ReservationForm()
    return render(request, 'reservations/make_reservation.html', {'form': form, 'restaurant': restaurant})

def reservation_success(request):
    return render(request, 'reservations/reservation_success.html')
