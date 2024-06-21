# Generated by Django 5.0.6 on 2024-06-21 16:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('base', '0003_remove_patient_user_alter_emergency_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='user',
        ),
        migrations.AddField(
            model_name='doctor',
            name='groups',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.group'),
        ),
        migrations.AddField(
            model_name='medicalrecord',
            name='pdf_file',
            field=models.FileField(blank=True, null=True, upload_to='medical_record/pdf/'),
        ),
    ]
