# Generated by Django 5.0.6 on 2024-05-29 03:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutordb', '0002_alter_attendance_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attendance',
            options={'managed': False},
        ),
    ]
