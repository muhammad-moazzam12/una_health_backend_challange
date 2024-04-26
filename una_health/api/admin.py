from django.contrib import admin

from .models import Customer, Device, GlucoseData

admin.site.register(Customer)
admin.site.register(Device)
admin.site.register(GlucoseData)
