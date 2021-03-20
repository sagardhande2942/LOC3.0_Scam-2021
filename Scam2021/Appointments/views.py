from django.shortcuts import render
from .models import *
from Auth.models import *
from .decorators import *
from django.contrib.auth.decorators import login_required
import datetime

@login_required
@user_is_patient
def book(request, doctor_id):
    try:
        patient = Patient.objects.get(user_id_id = request.user.id)
        doctor = Doctor.objects.get(id = doctor_id)
    except Patient.DoesNotExist or Doctor.DoesNotExist:
        raise PermissionDenied

    appointments_all = Appointment.objects.all()
    for appointment_all in appointments_all:
        if appointment_all.date == datetime.date(request.POST.get('date')) and doctor_id == appointment_all.doctor_id:
            if (appointment_all.time - datetime.time(request.POST.get('time')) < 30*60) or (datetime.time(request.POST.get('time')) - appointment_all.time < 30*60):
                return render(request, template_name = '', context={})
    appointment = Appointment.objects.create(patient_id = patient,
    doctor_id = doctor,
    date = request.POST.get('date'),
    time = request.POST.get('time'),
    is_approved = None,
    reason = request.POST.get('reason'),
    prior_reports = request.POST.get('prior_reports'))
    
    return render(request, template_name= '', context={'appointment' : appointment})


@login_required
@user_is_patient
def find_doctor(request):    
    doctors = Doctor.objects.all()
    return render(request, template_name = '', context = {'doctors': doctors})


    
@login_required
@user_is_doctor
def approve(request):
    try:
        doctor = Doctor.objects.get(user_id_id = request.user.id)
    except Doctor.DoesNotExist:
        raise PermissionDenied
    doctor_appointments = Appointment.objects.filter(doctor_id = doctor, is_approved = None)
    return render(request, template_name= '', context={'doctor_appointments': doctor_appointments})


    """
    TEMPLATE JINJA CODE

    for doctor_appointment in doctor_appointments:
    if <select tick>:
        doctor_appointment.is_approved = True 
        doctor_appointment.save(update = True)
    else:
        doctor_appointment.is_approved = False
        doctor_appointment.save(update = True)
    """

# Create your views here.
