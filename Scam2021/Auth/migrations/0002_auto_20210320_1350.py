# Generated by Django 3.1.7 on 2021-03-20 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='d_id',
            new_name='user_id',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='p_id',
            new_name='user_id',
        ),
    ]
