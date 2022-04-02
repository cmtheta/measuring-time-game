from django.test import TestCase
from django.http import HttpRequest
from django.urls import resolve
from gameapp.views import top, game, game_record, game_ranking

# Create your tests here.

class TopPageViewTest(TestCase):
    def test_top_returns_200(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    
    def test_top_returns_expected_content(self):
        response = self.client.get("/")
        self.assertEqual(response.content, b'Hello World')

class GameTest(TestCase):
    def test_should_resolve_game(self):
        found = resolve("/gameapp/")
        self.assertEqual(game, found.func)

class GameRecordTest(TestCase):
    def test_should_resolve_game(self):
        found = resolve("/gameapp/users/1/")
        self.assertEqual(game_record, found.func)

class GameRankingTest(TestCase):
    def test_should_resolve_game(self):
        found = resolve("/gameapp/ranking/")
        self.assertEqual(game_ranking, found.func)

