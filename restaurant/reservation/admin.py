from django.contrib import admin
from . models import Reservation

# Register your models here.

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('phone',)
    search_fields = ('date',)
    ordering = ('time',)
    
admin.site.register(Reservation,ReservationAdmin)



