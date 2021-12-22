from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
# from django.contrib.auth import get_user_model
from .models import User
# import collections
# from django.contrib.auth.models import Permission
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from userapp.decorator import user_type_hr, user_type_employee

@staff_member_required(login_url='/')
def admin_home(request):
    name = request.user.username
    return render(request,'manager_template/home_content.html',{'name':name})

@login_required
@user_type_hr
def hr_home(request,user):
    print('hkjb====================================hvkgeszrtg')
    name = request.user.username
    # id = request.user.id
    return render(request,'manager_template/hr_content.html',{'user':user,'name':name})

@login_required
@user_type_employee
def employee_home(request,user):
    print('emnfkvblir===============')
    name = request.user.username
    return render(request,'manager_template/employee_content.html',{'user':user,'name':name})

@staff_member_required(login_url='/')
def add_staff(request):
    name = request.user.username
    return render(request,'manager_template/add_staff_template.html',{'name':name})

@staff_member_required(login_url='/')
def manage_staff(request):
    name = request.user.username
    response = User.objects.exclude(user_type='Manager').order_by('-user_type')
    col = ['id','username','first_name','last_name','email','user_type']
    return render(request,'manager_template/manage_staff_template.html', {'response':response,'name':name, 'col':col})

@login_required
@user_type_hr
def add_employee(request,user):
    print(user)
    name = request.user.username
    return render(request,'manager_template/add_employee_template.html',{'user':user,'name':name})

@login_required
@user_type_hr
def manage_employee(request,user):
    # response = User.objects.order_by('-user_type')
    response = User.objects.filter(user_type='Employee')
    # name = User.objects.get(username='username')
    name = User.objects.filter(user_type='HR')
    # print(request.user.username)
    name = request.user.username
    # name = name[17:-3]
    col = ['id','username','first_name','last_name','email']
    return render(request,'manager_template/manage_employee_template.html', {'response':response,'name':name, 'col':col, 'user':user})

@staff_member_required(login_url='/')
def user_delete(request, id):
    try:
        user = User.objects.get(id=id)
        user.delete()
        messages.success(request, "Staff deleted Successfully!")
    except:
        messages.error(request, "Staff Not found")    
    return HttpResponseRedirect('/manage_staff')

@staff_member_required(login_url='/')
def user_update(request,id):
    name = request.user.username
    user = User.objects.get(id=id)
    print(user)
    return render(request, 'manager_template/update_staff_template.html',{'user':user,'name':name})

@login_required
@user_type_employee
def employee_update(request,user):
    name = request.user.username
    # print(id)
    return render(request, 'manager_template/update_employee_template.html',{'user':user,'name':name})

@login_required
@user_type_employee
def update_employee_save(request,user):
    print("=============== calling update_employee_save ===============",user)
    id = request.user.id
    user = User.objects.get(id=id)
    if request.method == 'POST':
        print(request)
        user_type = request.user.user_type
        print("=============== Employee calling else ===============")
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        try:
            print("=============== Employee calling try ===============")
            print(request.POST['username'])
            User.objects.filter(id=id).update(first_name=first_name, last_name=last_name,username=username, email=email, is_staff=False)
            print("=============== Hr calling try2 ===============")
            messages.success(request,'User Updated Successfully')
            return HttpResponseRedirect('/employee_update/%s'%user_type)   
        except:
            messages.error(request,'Failed to Update User!')
            return HttpResponseRedirect('/employee_update/%s'%user_type)

@staff_member_required(login_url='/')
def update_staff_save(request,id):
    print("=============== calling update_staff_save ===============",id)
    if request.method == 'POST':
        print(request)
        print("=============== Hr calling else ===============")
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        user_type = request.POST.get('user_type')
        try:
            print("=============== Hr calling try ===============")
            print(request.POST['username'])
            User.objects.filter(id=id).update(first_name=first_name, last_name=last_name,username=username, email=email, user_type=user_type, is_staff=False)
            print("=============== Hr calling try2 ===============")
            messages.success(request,'User Updated Successfully')
            return HttpResponseRedirect('/manage_staff')   
        except:
            messages.error(request,'Failed to Update User!')
            return HttpResponseRedirect('/manage_staff')

@staff_member_required(login_url='/')
def employee_delete(request, id):
    try:
        user = User.objects.get(id=id)
        user.delete()
        messages.success(request, "Employee deleted Successfully!")
    except:
        messages.error(request, "Employee Not found")    
    return render(request, 'manager_template/manage_employee_template.html')



@login_required
def userlogout(request):
    logout(request)
    return redirect('/')

@staff_member_required(login_url='/')
def add_staff_save(request):
    if request.method != 'POST':
        return HttpResponse('Method Not Allowed!')
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_type = request.POST.get('user_type')
        try:
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password, user_type=user_type, is_staff=False)
            user.save()
            messages.success(request,'Successfully Added User')
            return HttpResponseRedirect('/add_staff')   
        except:
            messages.error(request,'Failed to Add User!')
            return HttpResponseRedirect('/add_staff')

@login_required
@user_type_hr
def add_employee_save(request,user):
    if request.method != 'POST':
        return HttpResponse('Method Not Allowed!')
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # user_type = request.POST.get('user_type')
        try:
            emp = User.objects.create_user(first_name=first_name, last_name=last_name, username=username,\
                 email=email, password=password, user_type='Employee', is_staff=False)
            emp.save()
            messages.success(request,'Successfully Added User')
            return HttpResponseRedirect('/manage_employee/%s'%user)       
        except:
            messages.error(request,'Failed to Add User!')
            return HttpResponseRedirect('/add_employee/%s'%user)