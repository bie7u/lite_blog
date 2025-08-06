from django.test import TestCase
from django.utils import timezone
from datetime import date, timedelta
from blog.models import League, Season, Team, Match, Standing


class StandingRecalculationTest(TestCase):
    def setUp(self):
        # Create test data
        self.league = League.objects.create(
            name="Test League",
            slug="test-league",
            country="Test Country"
        )
        
        self.season = Season.objects.create(
            league=self.league,
            name="2023-24",
            start_date=date(2023, 8, 1),
            end_date=date(2024, 5, 31),
            is_active=True
        )
        
        self.team1 = Team.objects.create(
            name="Team One",
            slug="team-one",
            short_name="T1"
        )
        
        self.team2 = Team.objects.create(
            name="Team Two",
            slug="team-two",
            short_name="T2"
        )
        
        # Create standings
        self.standing1 = Standing.objects.create(
            season=self.season,
            team=self.team1
        )
        
        self.standing2 = Standing.objects.create(
            season=self.season,
            team=self.team2
        )
    
    def test_standings_recalculation(self):
        """Test that standings are recalculated correctly based on match results"""
        # Create a finished match where team1 beats team2 2-1
        match = Match.objects.create(
            season=self.season,
            home_team=self.team1,
            away_team=self.team2,
            home_score=2,
            away_score=1,
            status='finished',
            match_date=timezone.now()
        )
        
        # Recalculate standings
        Standing.recalculate_standings(self.season)
        
        # Refresh from database
        self.standing1.refresh_from_db()
        self.standing2.refresh_from_db()
        
        # Check team1 stats (winner)
        self.assertEqual(self.standing1.matches_played, 1)
        self.assertEqual(self.standing1.wins, 1)
        self.assertEqual(self.standing1.draws, 0)
        self.assertEqual(self.standing1.losses, 0)
        self.assertEqual(self.standing1.goals_for, 2)
        self.assertEqual(self.standing1.goals_against, 1)
        self.assertEqual(self.standing1.points, 3)
        self.assertEqual(self.standing1.goal_difference, 1)
        
        # Check team2 stats (loser)
        self.assertEqual(self.standing2.matches_played, 1)
        self.assertEqual(self.standing2.wins, 0)
        self.assertEqual(self.standing2.draws, 0)
        self.assertEqual(self.standing2.losses, 1)
        self.assertEqual(self.standing2.goals_for, 1)
        self.assertEqual(self.standing2.goals_against, 2)
        self.assertEqual(self.standing2.points, 0)
        self.assertEqual(self.standing2.goal_difference, -1)
        
        # Check ordering (team1 should be first)
        standings = Standing.objects.filter(season=self.season).order_by('order')
        self.assertEqual(standings[0].team, self.team1)
        self.assertEqual(standings[1].team, self.team2)
    
    def test_live_match_included_in_standings(self):
        """Test that live matches are included in standings calculation"""
        # Create a live match
        match = Match.objects.create(
            season=self.season,
            home_team=self.team1,
            away_team=self.team2,
            home_score=1,
            away_score=0,
            status='live',
            match_date=timezone.now()
        )
        
        # Recalculate standings
        Standing.recalculate_standings(self.season)
        
        # Refresh from database
        self.standing1.refresh_from_db()
        
        # Check that live match is counted
        self.assertEqual(self.standing1.matches_played, 1)
        self.assertEqual(self.standing1.points, 3)
    
    def test_scheduled_match_not_included(self):
        """Test that scheduled matches are not included in standings"""
        # Create a scheduled match
        match = Match.objects.create(
            season=self.season,
            home_team=self.team1,
            away_team=self.team2,
            home_score=0,
            away_score=0,
            status='scheduled',
            match_date=timezone.now() + timedelta(days=1)
        )
        
        # Recalculate standings
        Standing.recalculate_standings(self.season)
        
        # Refresh from database
        self.standing1.refresh_from_db()
        
        # Check that scheduled match is not counted
        self.assertEqual(self.standing1.matches_played, 0)
        self.assertEqual(self.standing1.points, 0)
