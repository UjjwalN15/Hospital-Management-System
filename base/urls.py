from django.urls import path
from .views import *
urlpatterns = [
    path('patient/', PatientApiView.as_view({'get': 'list','post':'create'}),name='patient'),
    path('patient/<int:pk>/', PatientApiView.as_view({'get': 'retrieve', 'put':'update','patch': 'partial_update', 'delete':'destroy'}),name='patient'),
    path('speciality/', Doctor_SpecialityApiView.as_view({'get': 'list','post':'create'}),name='speciality'),
    path('speciality/<int:pk>/', Doctor_SpecialityApiView.as_view({'get': 'retrieve', 'put':'update','patch': 'partial_update', 'delete':'destroy'}),name='speciality'),
    path('doctor/', DoctorApiView.as_view({'get': 'list','post':'create'}),name='doctor'),
    path('doctor/<int:pk>/', DoctorApiView.as_view({'get': 'retrieve', 'put':'update','patch': 'partial_update', 'delete':'destroy'}),name='doctor'),
    path('staffrole/', Staff_RoleApiView.as_view({'get': 'list','post':'create'}),name='staffrole'),
    path('staffrole/<int:pk>/', Staff_RoleApiView.as_view({'get': 'retrieve', 'put':'update','patch': 'partial_update', 'delete':'destroy'}),name='staffrole'),
    path('staff/', StaffApiView.as_view({'get': 'list','post':'create'}),name='staff'),
    path('staff/<int:pk>/', StaffApiView.as_view({'get': 'retrieve', 'put':'update','patch': 'partial_update', 'delete':'destroy'}),name='staff'),
    path('appointment/', AppointmentApiView.as_view({'get': 'list','post':'create'}),name='appointment'),
    path('appointment/<int:pk>/', AppointmentApiView.as_view({'get': 'retrieve', 'put':'update','patch': 'partial_update', 'delete':'destroy'}),name='appointment'),
    path('medical_record/', MedicalRecordApiView.as_view({'get': 'list','post':'create'}),name='medical_record'),
    path('medical_record/<int:pk>/', MedicalRecordApiView.as_view({'get': 'retrieve', 'put':'update','patch': 'partial_update', 'delete':'destroy'}),name='medical_record'),
    path('emergency/', EmergencyApiView.as_view({'get': 'list','post':'create'}),name='emergency'),
    path('emergency/<int:pk>/', EmergencyApiView.as_view({'get': 'retrieve', 'put':'update','patch': 'partial_update', 'delete':'destroy'}),name='emergency'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/',Login, name='login'),
    path('register/',register, name='register'),
    path('role/',groups, name='groups'),
]