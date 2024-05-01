from django.contrib import admin

from .models import Admin,Artist,Customer,Artwork, AuctionItem ,product


admin.site.register(Admin)
admin.site.register(Artist)
admin.site.register(Customer)
admin.site.register(Artwork)
admin.site.register(product)
admin.site.register(AuctionItem)