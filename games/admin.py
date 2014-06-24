from django.contrib import admin
from games.models import Player, Game, Frame, FinalFrame

class GameInline(admin.TabularInline):
    model = Game
    extra = 1

class FrameInline(admin.StackedInline):
    model = Frame
    extra = 0

class FinalFrameInline(admin.StackedInline):
    model = FinalFrame
    extra = 0

class FrameAdmin(admin.ModelAdmin):
    list_display = ('frame_number', 'closed', 'balls', 'ball_1', 'ball_2', 'partial_score')

class FinalFrameAdmin(admin.ModelAdmin):
    list_display = ('frame_number', 'closed', 'balls', 'ball_1', 'ball_2', 'fill_ball', 'partial_score')

class GameAdmin(admin.ModelAdmin):
    inlines = [FrameInline]
    list_display = ('play_date' ,'player', 'lane', 'score', 'completed')

class PlayerAdmin(admin.ModelAdmin):
    inlines = [GameInline]
    list_display = ('nickname', 'average')

admin.site.register(Frame, FrameAdmin)
admin.site.register(FinalFrame, FinalFrameAdmin)  
admin.site.register(Game, GameAdmin)
admin.site.register(Player, PlayerAdmin)
