from django.shortcuts import render
from django.contrib import messages
from .models import PatientMedicalRecord

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
    queryset_list = Listing.objects.order_by('-list_date')
    # keywords search
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter( description__icontains=keywords)
    #city
    
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__icontains=city)

    context = { 
    'listings' : queryset_list, 
    'state_choice': state_choice,
    'city_choice': city_choice,
    'Values' : request.GET
    }
    return render(request, 'listing/search.html', context)