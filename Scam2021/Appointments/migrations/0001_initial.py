# Generated by Django 3.1.7 on 2021-03-20 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('is_approved', models.BooleanField(blank=True, null=True)),
                ('reason', models.TextField(blank=True, max_length=1024, null=True)),
                ('prior_reports', models.ImageField(upload_to='')),
                ('is_alerted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='DoctorAppointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_alerted', models.BooleanField(default=False)),
                ('appointment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Appointments.appointment')),
            ],
        ),
    ]
