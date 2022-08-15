from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.utils import timezone


class TeacherExtra(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    salary = models.PositiveIntegerField(null=False)
    joindate = models.DateField(auto_now_add=True)
    mobile = models.CharField(max_length=40)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.user.first_name

    @property
    def get_id(self):
        return self.user.id

    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name


classes = [('one', 'one'), ('two', 'two'), ('three', 'three'), ('four', 'four'), ('five', 'five'), ('six', 'six'),
           ('seven', 'seven'), ('eight', 'eight'), ('nine', 'nine'), ('ten', 'ten')]


class StudentExtra(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    admin_file = models.CharField(max_length=10, default=None)
    withdrawal_file = models.CharField(max_length=10, default=None)
    tc_no = models.CharField(max_length=9, null=True)
    father_name = models.CharField(max_length=55, default=None)
    mother_name = models.CharField(max_length=55, default=None)
    occupation = models.CharField(max_length=25, default=None)
    address = models.CharField(max_length=100, default=None)
    last_inst = models.CharField(max_length=50, default=None)
    dob = models.DateField(default=timezone.now)
    date_of_joining = models.DateField(default=timezone.now)
    session = models.CharField(max_length=10, default=None)
    contact = models.CharField(max_length=40, null=True)
    fee = models.PositiveIntegerField(null=True)
    cl = models.CharField(max_length=10, choices=classes, default='one')
    status = models.BooleanField(default=False)

    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name

    @property
    def get_id(self):
        return self.user.id

    def __str__(self):
        return self.user.first_name


class Attendance(models.Model):
    roll = models.CharField(max_length=10, null=True)
    date = models.DateField()
    cl = models.CharField(max_length=10)
    present_status = models.CharField(max_length=10)


class Notice(models.Model):
    date = models.DateField(auto_now=True)
    by = models.CharField(max_length=20, null=True, default='school')
    message = models.CharField(max_length=500)
