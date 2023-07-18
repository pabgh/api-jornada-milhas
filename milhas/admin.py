from django.contrib import admin
from milhas.models import Depoimento

class Depoimentos(admin.ModelAdmin):
    list_display = ('id', 'foto','depoimento', 'autor')
    list_display_links = ('id','autor')
    search_fields = ('nome',)
    list_per_page = 10

admin.site.register(Depoimento, Depoimentos)