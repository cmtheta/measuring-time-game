from django.urls import path

from gameapp import views

urlpatterns = [
    path("", views.game , name="game"),
    path("users/<int:user_id>/", views.game_record , name="game_record"),
    path("ranking/", views.game_ranking , name="game_ranking"),
]