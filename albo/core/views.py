from django.shortcuts import render


def public(request):
    return render(request,'public/index.html')

def login(request):
    return render(request,'public/login.html')


def albo(request):
    return render(request,"albo/index.html",{})