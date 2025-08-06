from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from ordered_model.models import OrderedModel


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextUploadingField()
    description = models.CharField(max_length=255, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='articles')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class League(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    country = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Season(models.Model):
    league = models.ForeignKey(League, on_delete=models.CASCADE, related_name='seasons')
    name = models.CharField(max_length=100)  # e.g., "2023-24"
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['league', 'name']

    def __str__(self):
        return f"{self.league.name} - {self.name}"


class Team(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    short_name = models.CharField(max_length=10, blank=True)
    logo = models.ImageField(upload_to='team_logos/', blank=True)
    founded = models.IntegerField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Match(models.Model):
    MATCH_STATUS_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('live', 'Live'),
        ('finished', 'Finished'),
        ('postponed', 'Postponed'),
        ('cancelled', 'Cancelled'),
    ]

    season = models.ForeignKey(Season, on_delete=models.CASCADE, related_name='matches')
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_matches')
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_matches')
    home_score = models.IntegerField(default=0)
    away_score = models.IntegerField(default=0)
    status = models.CharField(max_length=20, choices=MATCH_STATUS_CHOICES, default='scheduled')
    match_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['season', 'home_team', 'away_team', 'match_date']

    def __str__(self):
        return f"{self.home_team.name} vs {self.away_team.name} - {self.season.name}"

    @property
    def winner(self):
        if self.status not in ['finished', 'live']:
            return None
        if self.home_score > self.away_score:
            return self.home_team
        elif self.away_score > self.home_score:
            return self.away_team
        return None  # Draw

    @property
    def is_draw(self):
        return self.status in ['finished', 'live'] and self.home_score == self.away_score


class Standing(OrderedModel):
    season = models.ForeignKey(Season, on_delete=models.CASCADE, related_name='standings')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='standings')
    matches_played = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    goals_for = models.IntegerField(default=0)
    goals_against = models.IntegerField(default=0)
    points = models.IntegerField(default=0)

    order_with_respect_to = 'season'

    class Meta:
        unique_together = ['season', 'team']
        ordering = ['season', 'order']

    def __str__(self):
        return f"{self.team.name} - {self.season.name} (Position {self.order})"

    @property
    def goal_difference(self):
        return self.goals_for - self.goals_against

    def calculate_stats_from_matches(self):
        """Calculate all stats based on matches for this team in this season"""
        home_matches = Match.objects.filter(
            season=self.season,
            home_team=self.team,
            status__in=['finished', 'live']
        )
        away_matches = Match.objects.filter(
            season=self.season,
            away_team=self.team,
            status__in=['finished', 'live']
        )

        # Reset stats
        self.matches_played = 0
        self.wins = 0
        self.draws = 0
        self.losses = 0
        self.goals_for = 0
        self.goals_against = 0
        self.points = 0

        # Process home matches
        for match in home_matches:
            self.matches_played += 1
            self.goals_for += match.home_score
            self.goals_against += match.away_score
            
            if match.home_score > match.away_score:
                self.wins += 1
                self.points += 3
            elif match.home_score == match.away_score:
                self.draws += 1
                self.points += 1
            else:
                self.losses += 1

        # Process away matches
        for match in away_matches:
            self.matches_played += 1
            self.goals_for += match.away_score
            self.goals_against += match.home_score
            
            if match.away_score > match.home_score:
                self.wins += 1
                self.points += 3
            elif match.away_score == match.home_score:
                self.draws += 1
                self.points += 1
            else:
                self.losses += 1

        self.save()

    @classmethod
    def recalculate_standings(cls, season):
        """Recalculate all standings for a given season based on match results"""
        standings = cls.objects.filter(season=season)
        
        # Update each standing's stats
        for standing in standings:
            standing.calculate_stats_from_matches()
        
        # Get updated standings and sort by points, goal difference, goals for
        updated_standings = cls.objects.filter(season=season).extra(
            select={'goal_diff': 'goals_for - goals_against'}
        ).order_by('-points', '-goal_diff', '-goals_for')
        
        # Update positions using django-ordered-model
        for index, standing in enumerate(updated_standings):
            standing.to(index)

        return updated_standings
