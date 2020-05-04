from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.auth.models import User
from .filters import EventsFilter


def index(request):
    return render(request, 'index.html')


def by_type(request):
    events = Events.objects.all( )

    my_filter = EventsFilter(request.GET, queryset=events)
    events = my_filter.qs

    context = {'events': events, 'my_filter': my_filter}
    return render(request, 'new.html', context)



def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        user = authenticate(username=username, password=password, )

        if user is None:
            messages.info(request, 'Nazwa użytkownika lub hasło są nieprawidłowe')
        else:
            login(request, user)
            return redirect('home')

    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('login')


def register_page(request):
    forms = CreateUserForm()

    if request.method == "POST":
        forms = CreateUserForm(request.POST)
        if forms.is_valid():
            forms.save()
            user = forms.cleaned_data.get('username')
            messages.success(request, 'Konto dla ' + user + ' zostało utworzone')
            return redirect('login')

    context = {'forms': forms}
    return render(request, 'register.html', context)


def home(request):
    return render(request, 'home.html')


@login_required
def create_event(request):
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

    context = {'event': event}
    return render(request, 'event.html', context)


@login_required
def your(request, pk):
    user = User.objects.get(id=pk)
    print(user.username)
    events = Events.objects.filter(creatorName=user.username)

    context = {'events': events}

    return render(request, 'your.html', context)
