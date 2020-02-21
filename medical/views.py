from django.contrib import messages
from django.contrib.auth import login,logout,authenticate,get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import (CreateView,TemplateView)
from .models import MyUser
from .forms import MedicalCreationForm,PatientCreationForm
from MedicalRecord.models import PatientMedicalRecord

User = get_user_model



#ladning page not in use
def index(request):
    return render(request, 'index.html')

#login page this is landing page for now
def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password1')
        user = authenticate(email=email,password=password)
        if user is not None:
            login(request,user)
            messages.success(request, f'You Have Login !')
            if request.user.role == 'Doctor':
                return redirect('medical_index')
            if request.user.role == 'Patient':
                return redirect('patient_index')
        else:
            return redirect('login')
    else:
        return render(request,'registration/login.html')

#logout view
def logout_page(request):
    logout(request)
    return redirect('/')


#signup page 
def SignUpView(request):
    form = MedicalCreationForm
    forms = PatientCreationForm
    return render(request,'registration/signup.html', {'form':form, 'forms':forms})

#medical signup modal form
def medical_signup(request):
    form = MedicalCreationForm(request.POST or None)
    if request.method == "POST":

        if form.is_valid():
            form.save()
            return redirect('login')
    context = {
       'form':form,
    }
    return render(request, 'registration/signup.html', context)

#patient signup
def patient_signup(request):
    forms = PatientCreationForm(request.POST or None)
    if request.method == "POST":

        if forms.is_valid():
            forms.save()
            return redirect('login')
    context = {
       'forms':forms
    }
    return render(request, 'registration/signup.html', context)


#patient web page
@login_required
def patient_page(request):
    return render(request, 'home.html')


#medical index page
@login_required
def medical_page(request):
    medical_staff = MyUser.objects.count()
    patient_user = MyUser.objects.count()
    patient_medical_records = PatientMedicalRecord.objects.all()
    patient_records = PatientMedicalRecord.objects.all().count
    context = {
        'medical_staff':medical_staff,
        'patient_medical_records': patient_medical_records,
        'patient_user':patient_user,
        'patient_records':patient_records
    }
    return render(request, 'dashboard.html',context)