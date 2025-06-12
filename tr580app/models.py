from django.db import models

class Country(models.Model):
    image = models.ImageField(upload_to="country_images/")
    name = models.CharField(max_length=20)
    population = models.CharField(max_length=20)
    territory = models.CharField(max_length=20)
    avg_price = models.CharField(max_length=20)
    region = models.CharField(max_length=20)
    about = models.TextField()

    class Meta:
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.name
    
class City(models.Model):
    image = models.ImageField(upload_to="city_images/")
    name = models.CharField(max_length=20)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="cities")

    class Meta:
        verbose_name_plural = "Cities"

    def __str__(self):
        return self.name

class Package(models.Model):
    image = models.ImageField(upload_to="package_images/")
    name = models.CharField(max_length=20)
    price = models.IntegerField(default=0)
    check_ins = models.IntegerField(default=0)
    airplane = models.BooleanField(True)
    visit = models.BooleanField(True)

    def __str__(self):
        return self.name

class Information(models.Model):
    image = models.ImageField(upload_to="info_images/")
    title = models.CharField(max_length=150)
    info = models.TextField()
    t_guests = models.CharField(max_length=10)
    a_accomoditations = models.CharField(max_length=10)
    a_places = models.CharField(max_length=10)
    check_ins = models.CharField(max_length=10)
    content = models.TextField()

    def __str__(self):
        return self.title
    
class PriceRange(models.Model):
    st_price = models.FloatField(default=0, blank=True, null=True)
    fn_price = models.FloatField(default=0, blank=True, null=True)

    def __str__(self):
        return str(self.st_price) + str(self.fn_price)


class Offer(models.Model):
    image = models.ImageField(upload_to="offer_images/", blank=True, null=True)
    period = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    days = models.IntegerField(default=0)
    content = models.TextField()

    def __str__(self):
        return self.title

class Reservation(models.Model):
    name = models.CharField(max_length=50)
    phone = models.IntegerField(default=0)
    number_of_guests = models.CharField(max_length=5)
    date = models.DateField()
    destination = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Guest(models.Model):
    number = models.CharField(max_length=3)

    def __str__(self):
        return self.number

class SiteSettings(models.Model):
    ititle = models.CharField(max_length=100, blank=True, null=True)
    imiddle_title = models.CharField(max_length=100, blank=True, null=True)
    imiddle_content = models.TextField(blank=True, null=True)
    atitle = models.CharField(max_length=20, blank=True, null=True)
    amiddle_title = models.CharField(max_length=50, blank=True, null=True)
    amiddle_content = models.TextField(blank=True, null=True)
    adown_title = models.CharField(max_length=150, blank=True, null=True)
    adown_content = models.TextField(blank=True, null=True)
    dtitle = models.CharField(max_length=50, blank=True, null=True)
    dcontent = models.CharField(max_length=50, blank=True, null=True)
    dmiddle_title = models.CharField(max_length=50, blank=True, null=True)
    dmiddle_content = models.TextField(blank=True, null=True)
    rtitle = models.CharField(max_length=50, blank=True, null=True)
    rsubtitle = models.CharField(max_length=50, blank=True, null=True)
    rcontent = models.TextField(blank=True, null=True)
    phone = models.IntegerField(default=0, blank=True, null=True)
    email = models.EmailField(max_length=256, blank=True, null=True)
    adress = models.TextField(blank=True, null=True)
    rmiddleinfo = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Site Settings'

    def save(self, *args, **kwargs):
        if not self.id and SiteSettings.objects.exists():
            return None
        return super(SiteSettings,self).save(*args,**kwargs)

    def __str__ (self):
        return "Setting"