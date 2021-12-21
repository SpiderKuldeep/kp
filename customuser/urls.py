"""customuser URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls.static import static
# from customuser import settings
from userapp import views, ManagerViews
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('demo/', views.showDemoPage),
    path('admin/', admin.site.urls),
    path('', views.showLoginPage),
    path('doLogin', views.doLogin),
    path('logout', ManagerViews.userlogout,  name='logout'),
    path('admin_home', ManagerViews.admin_home),
    path('manage_staff', ManagerViews.manage_staff),
    path('manage_employee/<str:user>', ManagerViews.manage_employee),
    re_path(r'user_delete/(?P<id>[0-9]+)$', ManagerViews.user_delete, name='user_delete'),
    # re_path(r'employee_delete/(?P<id>[0-9]+)$', ManagerViews.employee_delete, name='employee_delete'),
    re_path(r'user_update/(?P<id>[0-9]+)$', ManagerViews.user_update, name='user_update'),
    # path('user_update', ManagerViews.user_update, name='user_update'),
    path('hr_home/<str:user>', ManagerViews.hr_home),
    path('employee_home/<str:user>', ManagerViews.employee_home),
    path('add_staff', ManagerViews.add_staff),
    path('add_employee/<str:user>', ManagerViews.add_employee, name='add_employee'),
    path('add_staff_save', ManagerViews.add_staff_save),
    path('add_employee_save/<str:user>', ManagerViews.add_employee_save),
    path('update_staff_save/<id>', ManagerViews.update_staff_save, name='update_staff_save'),
    # re_path(r'update_staff_save/(?P<id>[0-9]+)$', ManagerViews.update_staff_save, name='update_staff_save'),
    path('get_user_details/', views.GetUserDetails),
    path('logout_user', views.logout_user)
]
# +static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
