from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm, DocumentForm
from django.forms import inlineformset_factory
from .models import *

@login_required(login_url = 'login')
def home(request):
    orderformset = inlineformset_factory(User, Document, fields=('document',))


    _id = request.user.id
    _user = User.objects.get(id = _id)

    formset = orderformset(queryset = Document.objects.none() ,instance = _user)

    data = Document.objects.filter(user = request.user)
    
    if request.method == 'POST':
        formset = orderformset(request.POST, request.FILES, instance = _user)
        if formset.is_valid():
            formset.save()
            return redirect("home")
    return render(request, 'main/home.html', {'documentForm':formset, 'data':data, 'id':_id})

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

def delete(request, pk):
    doc = Document.objects.get(id = pk)
    if request.method == "POST":
        doc.delete()
        return redirect("/")
    return render(request, 'main/delete.html', {'doc':doc})