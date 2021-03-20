from django.db import models

class Users(models.Model):
    email = models.EmailField(default='')
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=20,default='',null = True, blank=True)
    lastname = models.CharField(max_length=20, default='',null = True, blank=True)
    password = models.CharField(max_length=30, default='')
    contact = models.IntegerField(default='',null = True, blank=True)

    def __str__(self):
        return self.firstname

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