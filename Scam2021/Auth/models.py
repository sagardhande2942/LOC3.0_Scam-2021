from django.db import models


class Users(models.Model):
    id = models.AutoField(primary_key=True, default='')
    first_name = models.CharField(max_length = 30, default='', null = True, blank=True)
    last_name = models.CharField(max_length = 30, default='', null = True, blank=True)
    email = models.EmailField(max_length = 30, default='', null = True, blank=True)
    password = models.CharField(max_length = 30, default='', null = True, blank=True)
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