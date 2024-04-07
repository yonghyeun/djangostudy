from django.shortcuts import render , redirect
# 회원가입 및 로그인 기능을 위한 라이브러리 import 

from django.contrib.auth.models import User 
from django.contrib import auth

# 로그인 상태를 확인하기 위한 라이브러리 import  
from django.contrib.auth.decorators import login_required

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
            return render(request,'login.html', {'error':'아이디나 비밀번호가 틀렸어! 혹은 서버에 존재하지 않거나 !'})
    else:
        return render(request,'login.html')

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect('home')
    return render(request,'signup.html')

def home(request): # / 에 접속시 사용할 로직
    if request.user.is_authenticated:
        # 로그인한 사용자의 이름을 템플릿에 전달
        return render(request, 'base.html', {'username': request.user.username})
    else:
        # 로그인하지 않은 사용자의 경우 다른 처리를 할 수 있음
        return render(request, 'base.html')


