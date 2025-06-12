from django.shortcuts import render, redirect
from django.conf.urls.static import static
from tr580app.models import (
    Country, City, Package, Information, PriceRange, Offer,
    Reservation, Guest, SiteSettings
)

def index(request):
    settings = SiteSettings.objects.first()
    countries = Country.objects.all()

    context = {
        "settings" : settings,
        "countries" : countries
    }

    return render(request, 'index.html', context)

def about(request):
    settings = SiteSettings.objects.first()
    countries = Country.objects.all()
    cities = City.objects.all()
    packages = Package.objects.all()
    info = Information.objects.first()

    context = {
        "settings" : settings,
        "countries" : countries,
        "cities" : cities,
        "packages" : packages,
        "info" : info
    }

    return render(request, 'about.html', context)

def deals(request):
    settings = SiteSettings.objects.first()
    cities = City.objects.all()
    countries = Country.objects.all()
    prices = PriceRange.objects.all()
    offers = Offer.objects.all()


    context = {
        "settings" : settings,
        "cities" : cities,
        "countries" : countries,
        "prices" : prices,
        "offers" : offers
    }

    return render(request, 'deals.html', context)

def reservations(request):
    settings = SiteSettings.objects.first()
    reservs = Reservation.objects.all()
    countries = Country.objects.all()
    cities = City.objects.all()
    guests = Guest.objects.all()

    if request.method == "POST":
        name = request.POST.get("Name")
        phone = request.POST.get("Number")
        guest = request.POST.get("Guests")
        date = request.POST.get("date")
        destination = request.POST.get("Destination")

        Reservation.objects.create(
            name = name,
            phone = phone,
            number_of_guests = guest,
            date = date,
            destination = destination
        )
        return redirect("reservations")

    context = {
        "settings" : settings,
        "cities" : cities,
        "reservs" : reservs,
        "countries" : countries,
        "guests" : guests
    }

    return render(request, 'reservation.html', context)