from django.urls import path

from gameapp import views

urlpatterns = [
    path("", views.game , name="game"),
    path("record/", views.game_record , name="game_record"),
]