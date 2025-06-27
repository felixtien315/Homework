from django.contrib import admin
from .models import NightMarket, Vendor, Food

admin.site.register(NightMarket)
admin.site.register(Vendor)
admin.site.register(Food)