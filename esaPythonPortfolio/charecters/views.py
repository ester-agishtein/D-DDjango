from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Charecter, Team
from .forms import CharecterForm, TeamForm
from django.urls import reverse, resolve

# Create your views here.


def display_charecters(request):
    charecters = Charecter.objects.all()
    context = {'charecters': charecters}
    return render(request, 'charecters.html', context=context)


def create_charecter(request):
    form = CharecterForm()
    if request.method == 'POST':
        form = CharecterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('charecters:charecter_success')
    context = {'form': form}

    return render(request, 'create_charecter.html', context=context)


def update_charecter(request, pk):
    charecter = Charecter.objects.get(id=pk)
    form = CharecterForm(instance=charecter)

    if request.method == 'POST':
        form = CharecterForm(request.POST, instance=charecter)
        if form.is_valid():
            form.save()
            return redirect('charecters:charecter_success')
    context = {'form': form}
    return render(request, 'create_charecter.html', context=context)


def delete_charecter(request, pk):
    charecter = Charecter.objects.get(id=pk)
    if request.method == "POST":
        charecter.delete()
        return redirect('charecters:display_charecters')
    context = {'item': charecter}
    return render(request, 'delete_charecter.html', context=context)


def charecter_success(request):
    return render(request, 'charecter_success.html')


def team_success(request):
    return render(request, 'team_success.html')


def create_team(request):
    form = TeamForm()
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('charecters:team_success')
    context = {'form': form}
    return render(request, 'create_team.html', context=context)


def update_team(request, pk):
    team = Team.objects.get(id=pk)

    form = TeamForm(instance=team)

    if request.method == 'POST':
        form = TeamForm(request.POST, instance=team)
        if form.is_valid():
            form.save()
            return redirect('charecters:team_success')
    context = {'form': form}
    return render(request, 'create_team.html', context=context)


def display_teams(request):

    teams = Team.objects.all()
    charecter_list = []
    for team in teams:
        team_id = team.id
        charecters = Charecter.objects.filter(team=team.id)
        for charecter in charecters:
            charecter_list.append(charecter.charecter_name)
    context = {'teams': teams, 'charecters': charecter_list}
    return render(request, 'teams.html', context=context)


def delete_team(request, pk):
    team = Team.objects.get(id=pk)
    if request.method == "POST":
        team.delete()
        return redirect('charecters:display_teams')
    context = {'item': team}
    return render(request, 'delete_team.html', context=context)
