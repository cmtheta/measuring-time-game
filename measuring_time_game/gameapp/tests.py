from django.test import TestCase
from django.http import HttpRequest
from django.urls import resolve
from gameapp.views import top, game, game_record, game_ranking

# Create your tests here.

# トップページに関するテスト
class TopPageViewTest(TestCase):
    def test_top_returns_200(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    
    def test_top_returns_expected_content(self):
        response = self.client.get("/")
        self.assertEqual(response.content, b'Hello World')

# ゲーム画面に関するテスト
class GameTest(TestCase):
    def test_should_resolve_game(self):
        found = resolve("/gameapp/")
        self.assertEqual(game, found.func)

# ゲーム記録画面に関するテスト
class GameRecordTest(TestCase):
    def test_should_resolve_game(self):
        found = resolve("/gameapp/users/1/")
        self.assertEqual(game_record, found.func)

# ランキング画面に関するテスト
class GameRankingTest(TestCase):
    def test_should_resolve_game(self):
        found = resolve("/gameapp/ranking/")
        self.assertEqual(game_ranking, found.func)

