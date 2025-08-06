from django.contrib import admin
from blog import models
from ordered_model.admin import OrderedModelAdmin


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'created_at']
    list_filter = ['category', 'created_at']
    search_fields = ['title', 'description']


@admin.register(models.League)
class LeagueAdmin(admin.ModelAdmin):
    list_display = ['name', 'country', 'created_at']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', 'country']


@admin.register(models.Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'short_name', 'city', 'founded']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', 'short_name', 'city']


@admin.register(models.Season)
class SeasonAdmin(admin.ModelAdmin):
    list_display = ['name', 'league', 'start_date', 'end_date', 'is_active']
    list_filter = ['league', 'is_active']
    search_fields = ['name', 'league__name']


@admin.register(models.Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ['home_team', 'away_team', 'home_score', 'away_score', 'status', 'match_date', 'season']
    list_filter = ['status', 'season', 'match_date']
    search_fields = ['home_team__name', 'away_team__name']
    
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        # Recalculate standings when a match is saved
        if obj.status in ['finished', 'live']:
            models.Standing.recalculate_standings(obj.season)


@admin.register(models.Standing)
class StandingAdmin(OrderedModelAdmin):
    list_display = ['team', 'season', 'order', 'matches_played', 'wins', 'draws', 'losses', 'points', 'goal_difference']
    list_filter = ['season']
    search_fields = ['team__name', 'season__name']
    readonly_fields = ['matches_played', 'wins', 'draws', 'losses', 'goals_for', 'goals_against', 'points']
    
    def goal_difference(self, obj):
        return obj.goal_difference
    goal_difference.short_description = 'Goal Diff'
    
    actions = ['recalculate_standings']
    
    def recalculate_standings(self, request, queryset):
        seasons = set(standing.season for standing in queryset)
        for season in seasons:
            models.Standing.recalculate_standings(season)
        self.message_user(request, f"Recalculated standings for {len(seasons)} season(s)")
    recalculate_standings.short_description = "Recalculate standings for selected teams' seasons"
