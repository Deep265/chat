from django.shortcuts import render

def login_redirect(request):
    return render(request,'login_redirect.html')

def logout_redirect(request):
    return render(request,'logout_redirect.html')