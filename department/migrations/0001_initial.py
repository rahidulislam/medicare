# Generated by Django 4.0 on 2021-12-23 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Department')),
                ('short_description', models.TextField(verbose_name='Short Description')),
                ('image', models.ImageField(blank=True, upload_to='department/')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Doctor Name')),
                ('designation', models.CharField(max_length=100, verbose_name='Doctor Designation')),
                ('image', models.ImageField(blank=True, upload_to='doctor/')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctor_department', to='department.department', verbose_name='Doctor Department')),
            ],
        ),
    ]