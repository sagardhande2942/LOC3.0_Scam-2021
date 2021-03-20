from django.db import models
from Auth.models import Patient, Doctor


class Appointment(models.Model):
    patient_id = models.ForeignKey(Patient, on_delete = models.CASCADE)
    doctor_id = models.ForeignKey(Doctor, on_delete= models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    is_approved = models.BooleanField(null = True, blank = True)
    reason = models.TextField(max_length=1024, blank = True, null = True)
    prior_reports = models.ImageField()
    is_alerted = models.BooleanField(default = False)

    def __str__(self):
        return self.id 


class DoctorAppointment(models.Model):
    doctor_id = models.ForeignKey(Doctor, on_delete = models.CASCADE)
    appointment_id = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    is_alerted = models.BooleanField(default = False)

    class Meta:
        unique_together = [
            'doctor_id',
            'appointment_id'
        ]

    def __str__(self):
        return self.id
