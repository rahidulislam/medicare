# Generated by Django 4.0 on 2021-12-22 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('short_description', models.TextField()),
                ('banner_image', models.ImageField(blank=True, upload_to='banner/')),
            ],
        ),
    ]
