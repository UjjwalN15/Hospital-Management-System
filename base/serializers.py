from rest_framework.serializers import ModelSerializer
from .models import *


class PatientSerializer(ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
        
class Doctor_SpecialitySerializer(ModelSerializer):
    class Meta:
        model = Doctor_Speciality
        fields = '__all__'
        
class DoctorSerializer(ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'
        
class Staff_RoleSerializer(ModelSerializer):
    class Meta:
        model = Staff_Role
        fields = '__all__'
        
class StaffSerializer(ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'
        
class AppointmentSerializer(ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'
        
class MedicalRecordSerializer(ModelSerializer):
    class Meta:
        model = MedicalRecord
        fields = '__all__'
        
class ItemsSerializer(ModelSerializer):
    class Meta:
        model = Items
        fields = '__all__'
        
class BillingSerializer(ModelSerializer):
    class Meta:
        model = Billing
        fields = '__all__'