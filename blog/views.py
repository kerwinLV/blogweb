from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    # return HttpResponse("欢迎访问我的官网")
    return render(request,'blog/index.html',context={
        "title":"我的博客",
        "welcome":"欢迎来到我的博客"
    })