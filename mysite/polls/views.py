from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
  return HttpResponse("안녕 반가워 너는 지금 polls index. 에 있어")



def sum(a,b):
  return a + b

print(sum(1 , 2))