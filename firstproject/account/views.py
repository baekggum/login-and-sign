from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import redirect
# Create your views here.

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method =='POST':
        if request.POST['Password1'] == request.POST['Password2']:
            user = User.objects.create_user(username=request.POST['Username'],password=request.POST['Password1'])
            auth.login(request,user)
            return redirect('/login/')
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['Password1']
        user = auth.authenticate(request,username = username, password = password)
        if user is not None:
            auth.login(request,user)
            return redirect('/signup/')
        else:
            return render(request, 'login.html', {'error':'username or password is incorrect'})
    else:
        return render(request, 'login.html')
