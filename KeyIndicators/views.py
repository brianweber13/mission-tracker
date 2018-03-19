from django.http import HttpResponse
from django.shortcuts import render

def login(request):
    context = { 'subtitle' : 'login'}
    return render(request, 'KeyIndicators/login.html', context)
