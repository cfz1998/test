from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.decorators.http import require_http_methods

# Create your views here.
def index(request):
    print("index试图")
    return HttpResponse("hello world!")


@require_http_methods(["POST"])
def login(request):
    return "登录成功"

