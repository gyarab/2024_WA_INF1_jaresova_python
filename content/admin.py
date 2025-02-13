from django.contrib import admin
from .models import Game, Category

class GameAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    date_hierarchy = 'came out on'
    search_fields = ['name', 'rating', 'about']

# Register your models here.
admin.site.register(Game,GameAdmin)
admin.site.register(Category)