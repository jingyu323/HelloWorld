from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect


def hello(request):
    return HttpResponse("Hello r  world ! ")

#项目中如果代码有改动，服务器会自动监测代码的改动并自动重新载入，所以如果你已经启动了服务器则不需手动重启


def helloView(request):
    context          = {}
    context['hello'] = 'Hello Test World!'
    return render(request, 'hello.html', context)

def getName(request):
    context          = {}
    name  = request.GET.get("name")
    context['hello'] = request.GET.get("name")
    if name == 'baidu':
        return HttpResponseRedirect('http://www.baidu.com/')
    else :
        return render(request, 'hello.html', context)





