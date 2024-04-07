우리는 지난 과정에서 `/login , /signup` 경로에 접근하면

보내줄 `HTML` 문서를 만들었다.

이제 해당 문서가 기능 하도록 변경해보자

# 로직 추가하기

```python
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
```

이렇게 작성후 회원가입에서 가입 버튼을 누르면 다음과 같은 오류가 발생한다.

![alt text](image.png)

이건 회원가입이나 로그인 시 `ID , PASSWORD` 가 네트워크에서 나쁜 의도를 가진 사람이 탈취해갈 가능성이 있으니 보안에 신경쓰라는 오류이다.

`login , signup` 문서에서 `CSRF` 문제를 해결하기 위해 다음과 같은 코드를 추가해주자

```html
{% extends 'base.html' %} {% block content %}
<div class="container">
  <h1>로그인</h1>
  <form method="POST" action="{% url 'login' %}">
    {% csrf_token %} ID : # 추가
    <input name="username" type="text" value="" />
    <br />
    <br />
    PW :
    <input name="password" type="password" value="" />
    <br />
    <br />
    <input class="btn btn-primary" type="submit" value="로그인" />
  </form>

  {% if error %} {{error}} {% endif %}
</div>

{% endblock %}
```

```html
{% extends 'base.html' %} {% block content %}

<div class="container">
  <h1>회원가입</h1>
  <form method="POST" action="{% url 'signup' %}">
    {% csrf_token %} ID : # 추가
    <input name="username" type="text" value="" />
    <br />
    <br />
    PW :
    <input name="password1" type="password" value="" />
    <br />
    <br />
    Confirm :
    <input name="password2" type="password" value="" />
    <br />
    <br />
    <input class="btn btn-primary" type="submit" value="회원가입" />
  </form>
</div>
{% endblock %}
```
