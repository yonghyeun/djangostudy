from django.shortcuts import render

# Create your views here.

def login(): # /login 에 접속시 사용할 로직
  pass

def logout(): # /logout 에 접속시 사용할 로직 
  pass

def signup(): # /signup 에 접속시 사용할 로직
  pass

def home(request): # / 에 접속시 사용할 로직
  return render(request,'base.html')