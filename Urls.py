Urls.py :

from django.contrib import admin
from django.urls import path
from . import views as mainView
from doctor import views as doctor
from patient import views as patient

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", mainView.index, name="index"),
    path("DoctorLogin/", mainView.DoctorLogin, name="DoctorLogin"),
    path("PatientLogin/", mainView.PatientLogin, name="PatientLogin"),
    path("PatientRegister/", mainView.PatientRegister, name="PatientRegister"),

    # Doctorviews
    path("DoctorLoginCheck/", doctor.DoctorLoginCheck, name="DoctorLoginCheck"),
    path("DoctorHome/", doctor.DoctorHome, name="DoctorHome"),
    path('RegisterPatientView/', doctor.RegisterPatientView, name='RegisterPatientView'),
    path('ActivaPatient/', doctor.ActivaPatient, name='ActivaPatient'),
    path('DoctorViewResults/', doctor.DoctorViewResults, name='DoctorViewResults'),
   

    # Patient Views
    path("PatientRegisterActions/", patient.PatientRegisterActions, name="PatientRegisterActions"),
    path("PatientLoginCheck/", patient.PatientLoginCheck, name="PatientLoginCheck"),
    path("PatientHome/", patient.PatientHome, name="PatientHome"),
    path("MentalStateCheck/", patient.MentalStateCheck, name="MentalStateCheck"),
]
