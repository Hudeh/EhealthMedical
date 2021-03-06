# Generated by Django 3.0.3 on 2020-02-20 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PatientMedicalRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('state', models.CharField(choices=[('Lagos', 'Lagos'), ('Abuja', 'Abuja')], max_length=50)),
                ('next_kin', models.CharField(max_length=50)),
                ('birth_date', models.DateField()),
                ('sex', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('allegies', models.CharField(choices=[('Dust', 'Dust'), ('Smoke', 'Smoke')], max_length=10)),
                ('current_symtomps', models.CharField(choices=[('Coughing', 'Coughing'), ('Headach', 'Headach')], max_length=10)),
                ('symtomps_complaint', models.TextField()),
                ('start_date', models.DateField()),
            ],
        ),
    ]
