from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Subject
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def loginfunc(request):
    if request.method == 'POST':
        email2 = request.POST['email']
        password2 = request.POST['password']
        user = authenticate(request, email=email2, password=password2)
        if user is not None:
            login(request, user)
            return redirect('/reservation/list')
        else:
            return render(request, 'login.html')
    return render(request,'login.html')

def logoutfunc(request):
    logout(request)
    return redirect('login')

