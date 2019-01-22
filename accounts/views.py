from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth


# reate your views here.
def login(request):
    if request.method == 'POST':
        user=auth.authenticate(username=request.POST.get('username'),password=request.POST.get('password'))
        #print(request.POST['username'])
        #print(request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('homepage')
        else:
            return render(request,'accounts/login.html',{'error':'User or Password Invalid'})

    else:
        return render(request,'accounts/login.html')
def signup(request):
#create user if password matches and user doesn't exist
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request,'accounts/signup.html',{'error':'User Already Exists!'})
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
                auth.login(request,user)
                return redirect('homepage')
        else:
            return render(request,'accounts/signup.html',{'error':'Password Mismatch!'})
    else:
        return render(request,'accounts/signup.html')
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
    return render(request,'accounts/signup.html')
