from django.contrib import admin
from mainapp.models import AddToCart, Checkout, Post, Replie, UserRating, SaveForLater
# Register your models here.

admin.site.register(UserRating)
admin.site.register(SaveForLater)
admin.site.register(Post)
admin.site.register(Replie)
admin.site.register(AddToCart)
admin.site.register(Checkout)
