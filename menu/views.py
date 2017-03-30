from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("this page wil display daily mess menu")
