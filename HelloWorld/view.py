from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello world ! ")

#项目中如果代码有改动，服务器会自动监测代码的改动并自动重新载入，所以如果你已经启动了服务器则不需手动重启