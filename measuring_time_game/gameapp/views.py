from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse

from gameapp.forms import RecordForm
from gameapp.models import Record
# Create your views here.

def top(request):
    return render(request, "gameapp/top.html")

def game(request):
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.created_by = request.user
            record.save()
            return redirect(game)
        else:
            print("Hello World")
    return render(request, "gameapp/game.html")

def game_record(request, user_id):
    return HttpResponse('ゲーム結果の閲覧')

def game_ranking(request):
    return HttpResponse('ランキングの閲覧')