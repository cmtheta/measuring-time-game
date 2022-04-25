from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from pkg_resources import require
from django.contrib.auth.decorators import login_required

from gameapp.forms import RecordForm
from gameapp.models import Record

def top(request):
    return render(request, "gameapp/top.html")

@login_required
def game(request):
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.created_by = request.user
            record.save()
            return redirect(game)
        else:
            pass
    else:
        return render(request, "gameapp/game.html")

@login_required
def game_record(request):
    user = request.user
    records = Record.objects.filter( created_by = user)
    return render(request, "gameapp/record.html", {"records" : records} )

