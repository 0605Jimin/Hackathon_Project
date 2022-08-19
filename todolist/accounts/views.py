from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/bad_login.html')
    # request == POST 로그인시키기
    else:
        return render(request, 'accounts/login.html')
    # request == GET login html 띄우기

def logout(request):
    auth.logout(request)
    return redirect('home')

def signup(request):
    if request.method == "POST":
        if request.POST['password'] == request.POST['repeat']:
            #회원가입
            new_user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
            #로그인
            auth.login(request, new_user)
            #홈 리다이렉션
            messages.success(request, "회원가입을 환영합니다.")
            return redirect('home')
    return render(request, 'accounts/register.html')
