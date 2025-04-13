
from django.contrib import admin
from .models import Blog, Profile

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_created')  
    search_fields = ('title', 'author')                 
    list_filter = ('date_created',)                     

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'biografia')                
    search_fields = ('user__username',)                 