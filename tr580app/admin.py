from django.contrib import admin
from tr580app.models import (
    Country, City, Package, Information, PriceRange, Offer,
    Reservation, Guest, SiteSettings
)

admin.site.register(Country)
admin.site.register(City)
admin.site.register(Package)
admin.site.register(Information)
admin.site.register(PriceRange)
admin.site.register(Offer)
admin.site.register(Reservation)
admin.site.register(Guest)
admin.site.register(SiteSettings)
