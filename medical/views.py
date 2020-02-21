from django.contrib import messages
from django.contrib.auth import login,logout,authenticate,get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import (CreateView,TemplateView)
from .models import MyUser
from .forms import MedicalCreationForm,PatientCreationForm


User = get_user_model

def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password1')
        user = authenticate(email=email,password=password)
        if user is not None:
            login(request,user)
            if request.user.role == 'Doctor':
                return redirect('medical_index')
            if request.user.role == 'Patient':
                return redirect('patient_index')
        else:
            return redirect('login')
    else:
        return render(request,'registration/login.html')

def logout_page(request):
    logout(request)
    return redirect('/')

def SignUpView(request):
    form = MedicalCreationForm
    forms = PatientCreationForm
    return render(request,'registration/signup.html', {'form':form, 'forms':forms})






def medical_signup(request):
    form = MedicalCreationForm(request.POST or None)
    if request.method == "POST":

        if form.is_valid():
            form.save()
            messages.success(request, f'Account Created')
            return redirect('login')
    context = {
       'form':form,
    }
    return render(request, 'registration/signup_form.html', context)

def patient_signup(request):
    forms = PatientCreationForm(request.POST or None)
    if request.method == "POST":

        if forms.is_valid():
            forms.save()
            messages.success(request, f'Account Created')
            return redirect('login')
    context = {
       'forms':forms
    }
    return render(request, 'registration/signup_form.html', context)


@login_required
def patient_page(request):
    return render(request, 'home.html')

@login_required
def medical_page(request):
    return render(request, 'dashboard.html')