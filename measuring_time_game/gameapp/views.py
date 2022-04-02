from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def top(request):
    return HttpResponse(b"Hello World")

def game(request):
    return HttpResponse('ゲーム画面')

def game_record(request):
    return HttpResponse('ゲーム結果の閲覧')

def game_ranking(request):
    return HttpResponse('ランキングの閲覧')