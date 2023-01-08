from django.contrib import admin
from . models import Blog , Category ,Tag , Comment
# Register your models here.

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment)

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','created_at','auther',)
    list_filter = ('auther',)
    search_fields = ('title',)
    ordering = ('created_at','title')
    
admin.site.register(Blog,BlogAdmin)
