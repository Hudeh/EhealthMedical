from django.shortcuts import render
from django.contrib import messages
from .models import PatientMedicalRecord




#patient medical record view
def MedicalRecord(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        sex = request.POST.get('sex')
        surname = request.POST.get('surname')
        state = request.POST.get('state')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        allegies = request.POST.get('allegies')
        current_symtomps = request.POST.get('current_symtomps')
        symtomps_complaint = request.POST.get('symtomps_complaint')
        start_date = request.POST.get('start_date')
        next_kin = request.POST.get('next_kin')
        birth_date = request.POST.get('birth_date')
        record_form = PatientMedicalRecord.objects.create(first_name=first_name,surname=surname,sex=sex,start_date=start_date,
                                                        birth_date=birth_date, current_symtomps=current_symtomps,
                                                        symtomps_complaint=symtomps_complaint, next_kin=next_kin,allegies=allegies                                                                      )
        record_form.save()
        messages.success(request, f'Your Appointment was Succesful')
    return render(request,'home.html')



def search(request):
    records = PatientMedicalRecord.objects.order_by('-created_at')

    if 'condition' in request.GET:
        keywords = request.GET['condition']
        if keywords:
            records = records.filter(condition__iexact=keywords)

    return render(request, 'medical_record.html', {'records': records})