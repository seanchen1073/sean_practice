from django.shortcuts import render

def index(request):
    return render(request, "bros/index.html")

def new(request):
    return render(request, "bros/new.html")
