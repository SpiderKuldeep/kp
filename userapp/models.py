from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save

class User(AbstractUser):
    user_type_data = ((1,'Manager'),(2,'HR'),(3,'Employee'))
    user_type = models.CharField(default='Manager', choices=user_type_data,max_length=10)

class AdminManager(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

class Staffs(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class Employees(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField()
    objects = models.Manager()
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == (1 or 'Manager'):
            AdminManager.objects.create(admin=instance)
        if instance.user_type == (2 or 'HR'):
            Staffs.objects.create(admin=instance)
        if instance.user_type == (3 or 'Employee'):
            Employees.objects.create(admin=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == (1 or 'Manager'):
        instance.adminmanager.save()
    if instance.user_type == (2 or 'HR'):
        instance.staffs.save()
    if instance.user_type == (3 or 'Employee'):
        instance.employees.save()