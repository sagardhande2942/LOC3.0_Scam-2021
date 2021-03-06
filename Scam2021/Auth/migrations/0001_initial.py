# Generated by Django 3.1.7 on 2021-03-20 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, default='', max_length=30, null=True)),
                ('last_name', models.CharField(blank=True, default='', max_length=30, null=True)),
                ('email', models.EmailField(blank=True, default='', max_length=30, null=True)),
                ('password', models.CharField(blank=True, default='', max_length=30, null=True)),
                ('contact', models.IntegerField(blank=True, default='', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Auth.users')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d_qualif', models.CharField(blank=True, choices=[('Dentist', 'Dentist'), ('Cardiologitst', 'Cardiologitst'), ('Cosmetic', 'Cosmetic')], max_length=30, null=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Auth.users')),
            ],
        ),
    ]
