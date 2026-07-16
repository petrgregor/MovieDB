from django.http import HttpResponse


def hello(request):
    return HttpResponse("Hello World!")


# http://127.0.0.1:8000/hello2/nice/
def hello2(request, s):
    return HttpResponse(f"Hello, {s} world!")


# http://127.0.0.1:8000/hello3?s=nice
def hello3(request):
    s = request.GET.get('s', '')
    return HttpResponse(f"Hello, {s} world!")


def hello4(request):
    html = "<html><body><h1>Hello World</h1></body></html>"
    return HttpResponse(html)


# http://127.0.0.1:8000/add/5/2/
def add(request, num1, num2):
    return HttpResponse(f"{num1} + {num2} = {num1+num2}")


# http://127.0.0.1:8000/add2?num1=500&num2=250
def add2(request):
    num1 = int(request.GET.get('num1', 0))
    num2 = int(request.GET.get('num2', 0))
    return HttpResponse(f"{num1} + {num2} = {num1+num2}")
