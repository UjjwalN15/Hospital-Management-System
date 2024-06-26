from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group
from django.utils.timezone import now



class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=300)
    password = models.CharField(max_length=300)
    groups = models.ManyToManyField(Group)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class Patient(models.Model):
    name = models.CharField(max_length=300)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=100,choices=[('male','Male'),('female','Female'),('others','Others')])
    address = models.CharField(max_length=300)
    phone = models.CharField(max_length=300)
    medical_history = models.TextField(blank=True)
    schedule = models.DateTimeField(default=now)

    
class Doctor_Speciality(models.Model):
    name = models.CharField(max_length=255)

class Doctor(models.Model):
    groups = models.OneToOneField(Group, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=300)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=100,choices=[('male','Male'),('female','Female'),('others','Others')])
    address = models.CharField(max_length=300)
    specialty = models.ForeignKey(Doctor_Speciality, on_delete=models.CASCADE)
    phone = models.CharField(max_length=300)

class Staff_Role(models.Model):
    name = models.CharField(max_length=255)

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=100,choices=[('male','Male'),('female','Female'),('others','Others')])
    address = models.CharField(max_length=300)
    role = models.ForeignKey(Staff_Role, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    status = models.CharField(max_length=100, choices=[('scheduled', 'Scheduled'), ('canceled', 'Canceled'), ('completed', 'Completed')])

def nepal_time_default():
    return now()

class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    diagnosis = models.TextField()
    treatments = models.TextField()
    prescriptions = models.TextField(blank=True)
    pdf_file = models.FileField(upload_to='medical_record/pdf/', null=True, blank=True)
    
    
class Emergency(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    contact_number = models.CharField(max_length=300)
    date = models.DateTimeField(default=nepal_time_default)
    
    

