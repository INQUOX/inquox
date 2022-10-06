from django.shortcuts import render

# Create your views here.

def to_login(request):
  return render(request, 'inquox_app/login.html')

def to_register(request):
  return render(request, 'inquox_app/register.html')