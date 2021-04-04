from django.db import models

# Create your models here.
class User(models.Model):

    fullname = models.CharField(max_length=32)
    username = models.CharField(max_length=32, unique=True)
    phone = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    website = models.CharField(max_length=128)

    street = models.CharField(max_length=32)
    suite = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    zipcode = models.CharField(max_length=32)
    geo_lat = models.CharField(max_length=32)
    geo_lng = models.CharField(max_length=32)

    company_name = models.CharField(max_length=32)
    company_catchPhrase = models.CharField(max_length=128)
    company_bs = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, username={self.username!r}, is_staff={self.is_staff})"

    def __repr__(self):
        return str(self)
