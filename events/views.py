from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'index.html')


def new(request):
    events = Events.objects.all()
    return render(request, 'new.html', {'events': events})


def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        user = authenticate(username=username, password=password,)

        if user is None:
            messages.info(request, 'Nazwa użytkownika lub hasło są nieprawidłowe')
        else:
            login(request, user)
            return redirect('home')

    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')


def registerPage(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Konto dla ' + user + ' zostało utworzone')
            return redirect('login')

    context = {'form': form}
    return render(request, 'register.html', context)


def home(request):
    return render(request, 'home.html')

@login_required
def CreateEvent(request):
    form = CreateEventForm()

    if request.method == "POST":
        form = CreateEventForm(request.POST)
        if form.is_valid():
            form.save()
            event = form.cleaned_data.get('name')
            messages.success(request, 'Wydarzenie ' + event + ' zostało utworzone')
            return redirect('profile')

    context = {'form': form}
    return render(request, 'create.html', context)


@login_required
def profile(request):
    return render(request, 'profile.html')


@login_required
def event(request, pk):

    event = Events.objects.get(id=pk)

    context ={'event':event}
    return render(request, 'event.html', context)