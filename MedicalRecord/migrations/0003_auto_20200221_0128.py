# Generated by Django 3.0.3 on 2020-02-21 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalRecord', '0002_auto_20200221_0059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientmedicalrecord',
            name='symtomps_complaint',
            field=models.TextField(blank=True, null=True),
        ),
    ]
