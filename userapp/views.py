# import re
# from django.urls import re_path
# from channels.auth import login, logout
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from userapp.EmailBackEnd import EmailBackEnd
# Create your views here.
def showDemoPage(request):
    return render(request, 'demo.html')

def showLoginPage(request):
    return render(request, 'login.html')

def doLogin(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST.get('email'), password=request.POST.get('password'))
        login(request,user)
        print(user)
        if user.user_type == 'Manager':
            print(type(user.user_type),user.user_type)
            return HttpResponseRedirect('admin_home')
        elif user.user_type == 'HR':
            print(type(user.user_type),user.user_type)
            return HttpResponseRedirect('hr_home/%s'%user.user_type)
        elif user.user_type == 'Employee':
            print(type(user.user_type),user.user_type)
            return HttpResponseRedirect('employee_home/%s'%user.user_type)
        else:
            messages.error(request, 'Invalid Login')
            return HttpResponseRedirect('/')
    # else:
    #     return HttpResponseRedirect('/')
            

def GetUserDetails(request):
    if request.user!=None:
        return HttpResponse('user : ' + request.user.email + 'usertype : ' + request.user.user_type)
    else:
        return HttpResponse('Please Login First!!')

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')