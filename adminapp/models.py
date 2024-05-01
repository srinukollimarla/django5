from django.contrib.auth.models import User
from django.db import models

# Create your models here.
#Admin table
class Admin(models.Model):
    id=models.AutoField(primary_key=True)
    username = models.CharField(max_length=100,blank=False,unique=True)
    password = models.CharField(max_length=100,blank=False)

    class Meta:
        db_table = "admin_table"
    def __str__(self):
        return self.username

#Artist Table
class Artist(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100, blank=False)
    gender_choices = (("male", "male"), ("Female", "Female"), ("other", "other"))
    gender = models.CharField(max_length=10,choices=gender_choices)
    mobile = models.CharField(max_length=15)
    date_of_birth = models.DateField(null=True)
    art_choices = (("Painter", "painter"), ("sclupter", "sclupter"), ("illustrator", "illustrator"))
    category = models.CharField(max_length=25)
    def __str__(self):
        return self.name
    class Meta:
        db_table = "artist_table"


#Customer Table
class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False)
    gender = models.CharField(max_length=20, blank=False)
    mobilenumber = models.CharField(max_length=20, blank=False, unique=True)

    class Meta:
        db_table = "customer_table"

    def __str__(self):
        return self.name

class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    # You can add more fields to the cart model as needed, e.g., cart_items, total_price, etc.

    class Meta:
        db_table = "cart_table"

    def __str__(self):
        return f"Cart for {self.customer.name}"
from django.db import models

class Artwork(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='artwork_images/')

    def __str__(self):
        return self.title
# auction/models.py

from django.db import models

# models.py
from django.db import models

class AuctionItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='auction_images/')
    current_bid = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
class product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='artwork_products/')

    def __str__(self):
        return self.name