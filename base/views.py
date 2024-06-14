from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import *
# Create your views here.

class PatientApiView(ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class Doctor_SpecialityApiView(ModelViewSet):
    queryset = Doctor_Speciality.objects.all()
    serializer_class = Doctor_SpecialitySerializer

class DoctorApiView(ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class Staff_RoleApiView(ModelViewSet):
    queryset = Staff_Role.objects.all()
    serializer_class = Staff_RoleSerializer

class StaffApiView(ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

class AppointmentApiView(ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class MedicalRecordApiView(ModelViewSet):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer

class ItemsApiView(ModelViewSet):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer

class BillingApiView(ModelViewSet):
    queryset = Billing.objects.all()
    serializer_class = BillingSerializer
