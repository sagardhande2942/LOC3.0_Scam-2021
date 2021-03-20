from django.db import models
from django.contrib.auth.models import User 


class Users(User):
    contact = models.IntegerField(default='',null = True, blank=True)
    
    def __str__(self):
        return self.first_name

class Patient(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_id.firstname

class Doctor(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    spec = (
        ('Dentist', 'Dentist'),
        ('Cardiologitst','Cardiologitst'),
        ('Cosmetic', 'Cosmetic')
        )
    d_qualif = models.CharField(choices=spec,null = True, blank=True, max_length=30)

    def __str__(self):
        return self.user_id.firstname