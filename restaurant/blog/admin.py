from django.contrib import admin
from . models import Blog , Category ,Tag
# Register your models here.

admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Tag)

