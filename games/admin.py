from django.contrib import admin
from games.models import Player, Game, Frame

class GameInline(admin.TabularInline):
    model = Game
    extra = 1

class FrameInline(admin.StackedInline):
    model = Frame
    extra = 0

class FrameAdmin(admin.ModelAdmin):
    list_display = ('order', 'closed', 'ball_1', 'ball_2', 'fill_ball')

class GameAdmin(admin.ModelAdmin):
    inlines = [FrameInline]
    list_display = ('play_date' ,'player_id', 'lane', 'score', 'completed')

class PlayerAdmin(admin.ModelAdmin):
    inlines = [GameInline]
    list_display = ('nickname', 'average')

admin.site.register(Frame, FrameAdmin)    
admin.site.register(Game, GameAdmin)
admin.site.register(Player, PlayerAdmin)