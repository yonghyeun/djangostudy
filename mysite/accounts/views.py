from django.shortcuts import render , redirect
# 회원가입 및 로그인 기능을 위한 라이브러리 import 

from django.contrib.auth.models import User 
from django.contrib import auth


# Create your views here.


def signup(request):
    if request.method == "POST":
        if request.POST['password1']==request.POST['password2']:
            user=User.objects.create_user(request.POST['username'], password=request.POST['password1'])
            auth.login(request,user)
            return redirect('home')
    return render(request,'signup.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request,'login.html', {'error':'username or password is incorrect'})
    else:
        return render(request,'login.html')

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect('home')
    return render(request,'signup.html')

def home(request): # / 에 접속시 사용할 로직
  return render(request,'base.html')


# 기능이 작동하는지 확인해보자 

