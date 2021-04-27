from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm, DocumentForm
from .models import *

@login_required(login_url = 'login')
def home(request):
    form = DocumentForm()
    data = Document.objects.filter(user = request.user)
    for i in data:
        print(i.document)
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")
    return render(request, 'main/home.html', {'documentForm':DocumentForm(), 'data':data})

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'main/login.html', {})

def registerUser(request):
    form = CreateUserForm()

    if(request.method == 'POST'):
        form = CreateUserForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('login')

    return render(request, 'main/register.html', {'form':form})


def logoutUser(request):
    logout(request)
    return redirect('login')