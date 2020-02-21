from django import forms
from.models import PatientMedicalRecord



class MedicalRecordForm(forms.ModelForm):
    """A form for creating patient medical records """
    class Meta:
        model = PatientMedicalRecord
        fields = ('first_name', 'surname',  'next_kin', 'start_date',
                        'allegies', 'sex', 'symtomps_complaint', 'email', 'current_symtomps',
                        'birth_date', 'phone','state')
      