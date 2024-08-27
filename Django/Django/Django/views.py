from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello Avishek this is your first django server, Welcome")
    return render(request, "index.html")

def about(request):
    return HttpResponse("This is about page")

def disclaimer(request):
    return HttpResponse("This is disclamier page")