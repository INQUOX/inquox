from django.shortcuts import render

# Create your views here.

def to_login(request):
  context = {
    'title': 'Login'
  }
  return render(request, 'inquox_app/login.html', context=context)

def to_register(request):
  context = {
    'title': 'Registration'
  }
  return render(request, 'inquox_app/register.html', context=context)