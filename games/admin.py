from django.contrib import admin
from games.models import Player, Game

class GameInline(admin.TabularInline):
    model = Game
    extra = 1

class GameAdmin(admin.ModelAdmin):
    # fieldsets = [
    #     (None,               {'fields': ['question']}),
    #     ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    # ]

    list_display = ('play_date' ,'player_id', 'lane', 'score', 'completed')
    # list_filter = ['pub_date']
    # search_fields = ['question']

class PlayerAdmin(admin.ModelAdmin):
    inlines = [GameInline]
    list_display = ('nickname', 'average')
    
admin.site.register(Game, GameAdmin)
admin.site.register(Player, PlayerAdmin)