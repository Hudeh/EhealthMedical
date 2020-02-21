from django import forms
from.models import PatientMedicalRecord



class MedicalRecordForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    class Meta:
        model = PatientMedicalRecord
        fields = ('first_name', 'surname',  'next_kin', 'start_date',
                        'allegies', 'sex', 'symtomps_complaint', 'email', 'current_symtomps',
                        'birth_date', 'phone','state')
      