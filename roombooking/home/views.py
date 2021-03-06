from asyncio.windows_events import NULL
from pickle import FALSE
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import render,HttpResponse,redirect
from .modelsusers import users
#from django.contrib.auth.models import User , auth


def homepage(request):
    return render(request,'index.html',{'login':False})

def signup(request):
    if request.method=='POST':
        firstname=str(request.POST['firstname'])
        lastname=str(request.POST['lastname'])
        username=str(request.POST['username'])
        email=str(request.POST['email'])
        phone=str(request.POST['phone'])
        psw=str(request.POST['psw'])
        pswrepeat=str(request.POST['psw-repeat'])
        if pswrepeat==psw:
            if users.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('/signup')
            else:
                if users.objects.filter(email=email).exists():
                    messages.info(request,'Email Taken')
                    return redirect('/signup')
                else:
                    user=users()
                    user.firstname=firstname
                    user.lastname=lastname
                    user.username=username
                    user.psw=psw
                    user.phone=phone
                    user.email=email
                    user.save()
                    return redirect('/signin')

        else:
             messages.info(request,'Password not Matching')
             return redirect('/signup')
    else:    
        return render(request,'signup.html')

def signin(request):
    if request.method=='POST':
        global username
        username=str(request.POST['username'])
        psw=str(request.POST['psw'])
        if users.objects.filter(username=username).exists():
            a=users.objects.filter(username=username)
            if psw==a[0].psw:
                return render(request,'index.html',{'login':True,'firstname':users.objects.filter(username=username)[0].firstname,'username':users.objects.filter(username=username)[0].username})
            else:
                messages.info(request,'Enter correct password')
                return redirect('/signin')
        else:
            messages.info(request,'Username not Registered')
            return redirect('/signin')

    else:
        return render(request,'signin.html')


def logout_view(request):
    #logout(request)
    return redirect('/')


