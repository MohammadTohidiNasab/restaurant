from django.contrib import admin
from .models import Foods
# Register your models here.


class FoodsAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('rate',)
    search_fields = ('price',)
    ordering = ('time',)
    
admin.site.register(Foods,FoodsAdmin)