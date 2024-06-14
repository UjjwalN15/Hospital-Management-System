from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=300)
    password = models.CharField(max_length=300)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=100,choices=[('male','Male'),('female','Female'),('others','Others')])
    address = models.CharField(max_length=300)
    phone = models.CharField(max_length=300)
    medical_history = models.TextField(blank=True)

class Doctor_Speciality(models.Model):
    name = models.CharField(max_length=255)

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
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

class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    diagnosis = models.TextField()
    treatments = models.TextField()
    prescriptions = models.TextField(blank=True)
    
class Items(models.Model):
    name = models.CharField(max_length=300)
    price = models.PositiveIntegerField()

class Billing(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    items = models.ForeignKey(Items,on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=100, choices=[('paid', 'Paid'), ('unpaid', 'Unpaid')])
