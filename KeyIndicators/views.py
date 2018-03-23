from django.http import HttpResponse
# from django.http.HttpRequest import user
from django.shortcuts import render
from django.shortcuts import redirect

def home(request):
    if request.user.is_authenticated:
        context = { 'subtitle' : 'Home' }
        return render(request, 'KeyIndicators/base_body.html', context)
    else:
        return redirect('login')

def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        context = { 'subtitle' : 'Login' }
        return render(request, 'KeyIndicators/login.html', context)
