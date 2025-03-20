from django.contrib import admin
from .models import Game, Author, Rating, Comment

class GameAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    date_hierarchy = 'came_out_on'
    search_fields = ['name', 'rating', 'about', 'made_by']

# Register your models here.
admin.site.register(Game,GameAdmin)
admin.site.register(Author)
admin.site.register(Rating)
admin.site.register(Comment)