# `Recap`

우리는 지난 `docs` 에서 가상환경을 생성했고

VSCODE 터미널로 가상환경을 실행하는 방법을 배웠다.

그리고 프로젝트를 만드는 것 까지 성공했다.

이를 통해 우리는 `mysite` 라는 폴더를 생성했고

![alt text](image.png)

내부에 다음과 같은 여러 파일들을 생성했다.

기본적으로 프로젝트 생성 시 생성되는 파일들은 `django` 라이브러리 자체에서 본인들이 관리하는 코어 라이브러리라고 생각하자

우리가 원하는 기능을 만들기 위해선 이제 이 프로젝트를 커스터마이징해야 한다.

커스터마이징 하기 위한 폴더를 생성해보자

> ### 용어를 명확하게 정의하자
>
> 프로젝트를 만들면서 생성된 파일들을 `프로젝트` 라고 한다.
> 프로젝트만으로는 우리가 서비스를 제공 할 수 없다.
> 우리가 원하는 서비스가 담긴 폴더 , 혹은 그 이하의 논리적 구조를 앱 이라고 한다.

# 앱 만들기

### 가상환경 구동하기

> **가상환경을 구동하기 위해선 `VSCODE`의 터미널을 `cmd` 로 변경해줘야 한다.** > `VSCODE` 의 터미널은 여러 종류의 프롬프트를 지원한다.
> 이전 `docs` 에서 `VSCODE` 의 터미널을 `cmd` 터미널로 이동하는 방법을 소개했었다.

![alt text](image-1.png)

우선 앱을 만들기 전 가상환경을 꼭 켜두자

가상환경을 킨다는 것은 쉽게 말해

내 프로젝트를 위한 컴퓨터를 내가 사용하는 거라 생각하자

프로젝트들이 담긴 컴퓨터 앞에 내가 앉는 행위 자체가 , 가상환경을 키는거다.

가상환경을 킴으로서 우리는 프로젝트를 위한 컴퓨터의 전원을 켰다.

### 파일 폴더로 이동하기

가상환경을 키고 나면 현재 나의 경로는 가상환경 폴더에 존재한다.

위 경로를 보자 우리는 지금 `/myenv/Scripts` 폴더에 있다.

이제 우리가 생성한 폴더로 이동해주자

![alt text](image-2.png)

> 이동하기 위한 폴더명은 사용자에 따라 다를 수 있다. 잘 해보자

### `app` 만들기

![alt text](image-3.png)

`py maange.py startapp accounts` 를 이용하여 앱을 만들기 위한 폴더인 `accounts` 폴더를 생성해주자

![alt text](image-4.png)

`accounts` 폴더에는 우리가 원하는 기능을 구현하기 위한 로직들을 구현해주면 된다. :)

정말 고맙게도 `django` 에선 기본적인 앱들을 위해 필요한 파일들을 생성할 수 있는 명령어를 제공한다.

우리는 방금 회원가입 앱을 만들기 위해 필요한 파일들을 모두 생성해주었다.

### 코드를 치기 전 , 로직을 먼저 생각해보기

`django` 에서는 어떻게 웹 페이지를 만들까 ?

회원가입 서비스 예제를 통해 생각해보자

1. 사용자가 회원가입을 위한 주소로 접근한다. 예를 들어 접근 주소를 `/createuser` 라고 해보자

   > 웹에선 주소를 `/` 부터 시작한다.
   > 우리가 네이버 서버의 서버 관리자라고 생각해보자
   > 우리는 사용자들에게 `www.naver.com` 이란 주소를 기본적으로 제공하고 사용자가 네이버 카페에 접근 할 때 `www.naver.com/cafe` 로 접근한다.
   > 모든 접근에는 우리의 기본 서버 주소인 `www.naver.com` 이후 `/ ...` 이후의 주소로 접근 하기 때문에 서버 관리자 입장에선 `www.naver.com/cafe` 라고 치는 것보다 그냥 `/cafe` 만 입력하도록 한다.

2. 사용자가 `/craeteuser` 경로에 접근하게 되면 서버 측에 요청을 보내게 된다. (`reqeust`)

   > 사용자 : 야 서버 , 나 `/cafeuser` 에 접근했어 , 이 경로에는 어떤 정보가 있니 ?

3. 서버는 사용자가 접근한 주소를 기준으로 해당 주소에 맞는 정보를 제공해야 한다.

   > 서버 : 사용자의 요청이 `/craeteuser` 네 ? 해당 주소에는 회원가입 페이지를 전송해줘야지

4. 서버는 사용자에게 `/createuser` 에 해당하는 페이지 (`HTML` 문서) 를 제공한다.
   > `HTML` 문서는 웹페이지를 개발하는 언어라고 생각하자. :)

우리는 앞으로 이러한 로직을 코드로 구현 할 것이다.

# 회원가입 페이지를 만들어보자

### 프로젝트와 앱을 연동시켜주자

![alt text](image-5.png)

`mysite` 폴더에 존재하는 `settings.py` 파일을 열자

이거는 `django` 프로젝트의 설정과 관련된 설정을 모아둔 셋팅 파일이다.

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 추가
    'accounts' # 앱 폴더 (accounts) 와 프로젝트를 연동
]
```

해당 파일을 잘 찾다보면 `INSTALLED_APPS` 의 리스트에 우리가 만든 폴더명을 추가해주자

> `[]` 내부에 여러 값들을 모아둔 것을 리스트라고 한다. 리스트는 여러 데이터들을 모아두는 자료구조의 일종이다.

이를 통해 이제 우리의 프로젝트에서 우리의 앱인 `accounts` 를 등록시켜주었다.

> 엄밀히 말하면 등록시켰다는 것은 프로젝트에서 `accounts` 에 존재하는 데이터 , 파이썬 파일을 실행 가능하게 한다는 것을 의미한다.

# 회원가입 기능 구현하기

### 페이지의 주소와 로직을 담은 자료구조 생성하기 (`accounts`)

![alt text](image-6.png)

우선 `accounts` 폴더 내부에 `urls.py` 를 만들어주자

해당 파일이 의미하는 것은 다음과 같다.

**우리의 앱 (accounts) 에서 접근 가능한 경로들을 정의하고 해당 경로에서 사용할 로직들을 모아둔다**

우선 가볍게 이렇게만 생각하자

```python
from django.contrib import admin # django 에서 제공하는 라이브러리
from django.urls import path # django 에서 제공하는 라이브러리
from . import views # 현재 경로에 존재하는 views 파일을 불러온다

urlpatterns = [
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('signup/', views.signup, name="signup"),
]
```

다음과 같이 코드를 작성해주자

이것들이 무엇을 의미하는가 ?

위 `from , import` 구문은 `django` 에서 제공하는 라이브러리들과

`views.py` 라는 파일을 불러온 것이다.

> 아직 우리는 `views.py` 파일을 만들지 않았다. 나중에 만들어주도록 하자
> `from . ` 가 의미하는 것은 현재의 경로인 `.` 에 존재하는 이라 생각하면 편할 것 같다.
> 만약 폴더명인 `someFolder` 내부에 존재하는 파일을 가져올 것이라면 `from /someFolder` 이렇게 작성해야 할 것이다.

```python
urlpatterns = [
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('signup/', views.signup, name="signup"),
]
```

자 이부분은 어떤 것을 의미하냐면

`urlpatterns` 라는 리스트 `[]` 내부에서 `path(..)` 데이터들을 보관하겠다는 것을 의미한다.

```python
path('login/', # 사용할 주소 , login 주소에 접근하면
 views.login, # views 파일에 존재하는 login 이란 함수를 실행하자
 name="login"), # 이 path 의 이름은 login 이라 하자
```

### 페이지의 주소와 로직을 담은 자료구조 생성하기 (`project`)

자 우리는 위에서 우리의 앱에서 사용 할 `urlpatterns` 을 생성해주었다.

이제 프로젝트에서 사용할 `urlpatterns` 를 생성해주자

이번엔 `mysite/urls.py` 에 들어가 다음처럼 작성해주자

```python
from django.contrib import admin
from django.urls import path , include
import accounts.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/' , include('account.urls'))
]
```

`project` 의 `urlpatterns` 는 무엇을 의미하는가 ?

`path('accounts/' , include('account.urls'))`

내 프로젝트에서 사용할 `url` 경로에 따른 로직을 `accounts` 폴더 내에 존재하는 `urls.py` 파일에 정의된 로직을 사용하겠다는 것이다.

> `url 로직` ?
> 여태 설명했던 개념을 어떤 단어로 간지나게 포장한 것이다.
> 웹 페이지는 다음과 같은 기능을 해야 한다.
>
> - 어떤 주소에 접속하면 해당 주소에 맞는 페이지를 제공해야 한다.
> - 페이지들은 페이지에 걸맞는 기능을 해야 한다.
>   예를 들어 회원가입 페이지에 접속했다면, 회원가입 페이지가 나타나야 하며 회원가입 페이지는 회원가입 기능을 해야 한다.

# `Recap`

어려운 내용들이니 다시 회고하자

우리는 여태까지 무엇을 했는가 ?

1. `accounts` 폴더에 `urls.py` 파일을 생성했다.

해당 파일에선 `/login , /logout , /signup` 주소에 사용자가 접근했을 때

사용 할 로직들을 제공 할 수 있는 `urlpatterns` 를 만들어주었다.

```python
# accounts.urls.py
urlpatterns = [
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('signup/', views.signup, name="signup"),
]
```

2. `mysite` 폴더에 존재하는 `urls.py` 파일에 `accounts.urls.py` 를 연결시켜주었다.

```python
from django.contrib import admin
from django.urls import path , include
import accounts.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/' , include('account.urls'))
]
```

이를 통해 우리의 프로젝트는 우리의 앱 (`accounts`) 에서 정의된 `urlpatterns` 를 사용 할 수 있게 되었다.

이로서 우리는 **페이지의 주소 별 사용할 로직을 생성해주었다.**

### 페이지 구동을 위해 `accounts/view.js` 를 만들어주자

우선 자세한 로직은 나중에 사용하기로 하고

```python
# accounts.urls.py
urlpatterns = [
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('signup/', views.signup, name="signup"),
]
```

에서 사용할 `views.py` 파일과 내부에서 `login  , logout , signup` 함수들을 선언해두자

만들어두지 않으면 서버가 오류를 일으킨다.

> ![alt text](image-7.png)

```python
# accounts/view.py
from django.shortcuts import render

# Create your views here.

def login():
  pass

def logout():
  pass

def signup():
  pass
```

`pass` 는 함수 내부가 구현되지 않더라도 선언될 수 있도록 해두는 일종의 임시 장치이다.

나중에 저 부분을 로직으로 채워줄 것이다.

![alt text](image-8.png)

`view.py` 파일에서 함수들을 선언해주고 나서 서버를 열어보면 다음과 같은 서버의 모습이 보인다.

![alt text](image-9.png)

오류를 살펴보자

```
Using the URLconf defined in mysite.urls,
Django tried these URL patterns, in this order:

admin/
accounts/
The empty path didn’t match any of these.
```

너가 설정한 `URLconf` (프로젝트에서 사용하는 `urlpatterns`) 을 이용해서 페이지를 만드려고 했는데

해당 경로 (`/`) 에서 보여주거나 사용할 것이 아무것도 없어

> 비어있는 경로기 때문에 `/` 이다.

라고 이야기 한다.

`/` 에서 사용할 로직도 추가해주자

```python
# accounts/urls.py
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('signup/', views.signup, name="signup"),
    path('',views.home , name = 'home') # 빈 경로에 대한 로직 생성
]
```

```python
# mysite/urls.py
from django.contrib import admin
from django.urls import path , include
import accounts.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/' , include('accounts.urls')),
    path('', include('accounts.urls')) # 빈 경로에 대한 로직 생성
]
```

그리고 서버를 실행해보자

![alt text](image-10.png)

이번에 다른 오류가 뜬다 .이건 `views.py` 내부의 함수가 비어있기 때문에 발생하는 문제이며

함수의 내부를 채워주면 된다.

# 현재 내 서버는 작동을 하는지 보자

![alt text](image-11.png)

물론 오류가 뜨기하지만 맨 위의 로그를 보자

`GET / HTTP/1.1` !!

이것이 의미하는건 내 서버가 작동중이고

현재 내가 `/` 경로에 접속하는 요청이 서버에 들어왔단 것을 의미한다.

와우

이제 요청이 들어왔을 때 서버에서 건내줄 무엇인가를 만들어주면 된다.
