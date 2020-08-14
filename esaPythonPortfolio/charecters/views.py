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
            return redirect('charecters:success')
    context = {'form': form}

    return render(request, 'create_charecter.html', context=context)


def update_charecter(request, pk):
    charecter = Charecter.objects.get(id=pk)
    form = CharecterForm(instance=charecter)

    if request.method == 'POST':
        form = CharecterForm(request.POST, instance=charecter)
        if form.is_valid():
            form.save()
            return redirect('charecters:success')
    context = {'form': form}
    return render(request, 'create_charecter.html', context=context)


def delete_charecter(request, pk):
    charecter = Charecter.objects.get(id=pk)
    if request.method == "POST":
        charecter.delete()
        return redirect('charecters:display_charecters')
    context = {'item': charecter}
    return render(request, 'delete_charecter.html', context=context)


def success(request):
    print("sucsess request = ", request)
    return render(request, 'success.html')


def create_team(request):
    form = TeamForm()
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('charecters:success')
    context = {'form': form}
    return render(request, 'create_team.html', context=context)


def update_team(request, pk):
    team = Team.objects.get(id=pk)
    charecters = Charecter.objects.filter(team=team.id)
    print("charecter = ", charecters)
    form = TeamForm(instance=team)

    if request.method == 'POST':
        form = TeamForm(request.POST, instance=team)
        if form.is_valid():
            form.save()
            return redirect('charecters:success')
    context = {'form': form, 'charecters': charecters}
    return render(request, 'create_team.html', context=context)


def display_teams(request):
    teams = Team.objects.all()
    context = {'teams': teams}
    return render(request, 'teams.html', context=context)


def delete_team(request, pk):
    team = Team.objects.get(id=pk)
    if request.method == "POST":
        team.delete()
        return redirect('charecters:display_teams')
    context = {'item': team}
    return render(request, 'delete_team.html', context=context)
