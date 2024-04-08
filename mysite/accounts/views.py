from django.shortcuts import render , redirect
# 회원가입 및 로그인 기능을 위한 라이브러리 import 

from django.contrib.auth.models import User 
from django.contrib import auth , messages




# Create your views here.


def signup(request):
    if request.method == 'POST': # POST 요청에 대한 처리
        # 해당 username 이 데이터베이스에 존재하는지 확인
        if User.objects.filter(username = request.POST['username']).exists(): 
            return render(request,'signup.html',{'error' : '해당 회원 ID 가 존재합니다. 다른 아이디를 이용해주세요' })
        # 비밀번호와 확인 비밀번호가 일치 하지 않는다면 오류 메시지 렌더링 하기 
        if request.POST['password1'] != request.POST['password2']:
            return render(request,'signup.html',{'error' : '비밀번호와 확인 비밀번호가 일치하지 않습니다.' })
        # 모든 에러를 해결했다면 회원가입 완료하기
        new_user = User.objects.create_user( # 데이터베이스에 새로운 User 를 만들고 
            username=request.POST['username'],
            password=request.POST['password1']
        )
        auth.login(request, new_user) # 만들어진 새로운 유저를 로그인 시킴 
        return redirect('home')
    else: # GET 요청에 대한 처리
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


