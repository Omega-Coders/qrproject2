from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
def home(request):

    return render(request,'Scanner/index.html')
def signup(request):
    if request.method =="POST":
        username =request.POST["username"]
        emailid = request.POST['emailid']
        pass1 =request.POST['pass1']
        pass2 = request.POST["pass2"]


        myuser = User.objects.create_user(username,emailid,pass1)
        myuser.save()
        messages.success(request,"your are successfully logined")
        return redirect('signin')
    return render(request,'Scanner/signup.html')
def signin(request):
    if request.method=='POST':
        emailid=request.POST["emailid"]
        password1= request.POST["pass"]
        user = authenticate(email=emailid,password=password1)
        if user is not None:
            login(request,user)
            username1=user.name
            return render(request,"Scanner/index.html",{"username1":username1})
        else:
            messages.error(request,"invalid credentials!" )
            return redirect("home")


    return render(request,'Scanner/signin.html')
def signout(request):
    pass

# Create your views here.
