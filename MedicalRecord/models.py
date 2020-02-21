from django.db import models
from medical.choices import  GENDER, ALLEGIES, SYMTOMPS, STATE


class PatientMedicalRecord(models.Model):
    """ Medical record model"""
    first_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)
    state = models.CharField(max_length=50,choices=STATE)
    next_kin = models.CharField(max_length=50)
    birth_date = models.DateField()
    sex = models.CharField(max_length=10, choices=GENDER)
    allegies = models.CharField(max_length=10, choices=ALLEGIES)
    current_symtomps = models.CharField(max_length=10, choices=SYMTOMPS)
    symtomps_complaint = models.TextField(blank=True,null=True)
    start_date = models.DateField()
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    updated_on = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return self.first_name + ':' +self.current_symtomps
    