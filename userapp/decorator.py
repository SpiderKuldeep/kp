# from django.shortcuts import render
from django.http import HttpResponseRedirect
def user_type_hr(func):
    def inner(request,user):
        if request.user.user_type=='HR':
            print(request.user.user_type)
            return func(request,user)
        return HttpResponseRedirect('/')
    return inner

def user_type_employee(func):
    def inner(request,user):
        if request.user.user_type=='Employee':
            print(request.user.user_type)
            return func(request,user)
        return HttpResponseRedirect('/')
    return inner