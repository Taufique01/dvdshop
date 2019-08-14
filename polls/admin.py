from django.contrib import admin
from .models import Catagory,Movie,Basket,BasketDetails
# Register your models here.



admin.site.register(Catagory)
admin.site.register(Movie)
admin.site.register(Basket)
admin.site.register(BasketDetails)
