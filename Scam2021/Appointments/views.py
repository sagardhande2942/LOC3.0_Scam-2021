from django.shortcuts import render
from .models import *
from Auth.models import *
from .decorators import *
from django.contrib.auth.decorators import login_required


@login_required
@user_is_patient
def book(request):
    try:
        patient = Patient.objects.get(user_id_id = request.POST.get['user_id'])
        doctor = Doctor.objects.get(id = request.POST.get['doctor_id'])
    except Patient.DoesNotExist or Doctor.DoesNotExist:
        raise PermissionDenied

    appointment = Appointment.objects.create(patient_id = patient,
    doctor_id = doctor,
    date = request.POST.get['date'],
    time = request.POST.get['time'],
    is_approved = None,
    reason = request.POST.get['reason'],
    prior_reports = request.POST.get['prior_reports'])
    
    return render(request, template_name= '', context={'appointment' : appointment})

    

    
@login_required
@user_is_doctor
def approve(request):
    try:
        doctor = Doctor.objects.get(user_id_id = request.POST.get['user_id'])
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
