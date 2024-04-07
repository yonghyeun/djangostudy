from django.shortcuts import render

# Create your views here.

def login(request): # /login 에 접속시 사용할 로직
  return render(request,'login.html')

def logout(): # /logout 에 접속시 사용할 로직 
  pass

def signup(request): # /signup 에 접속시 사용할 로직
  return render(request,'signup.html')
  

def home(request): # / 에 접속시 사용할 로직
  return render(request,'base.html')