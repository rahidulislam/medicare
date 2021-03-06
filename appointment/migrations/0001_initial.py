# Generated by Django 4.0 on 2021-12-23 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('phone', models.CharField(max_length=50, verbose_name='Phone Number')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('appointment_date', models.DateField(verbose_name='Appointment Date')),
                ('note', models.TextField(verbose_name='Note')),
            ],
        ),
    ]
