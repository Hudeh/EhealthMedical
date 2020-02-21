from django.urls import include, path
from . import views
from MedicalRecord import recordviews

# all urls for both medical and patient signup and index page
urlpatterns = [
    path('', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('medical/signup', views.medical_signup, name='medical_signup'),
    path('index/patient', views.patient_page, name='patient_index'),
    path('patient/medical/record', recordviews.MedicalRecord, name='patient_medical_record'),
    path('index/medical', views.medical_page, name='medical_index'),
    path('patient/signup', views.patient_signup, name='patient_signup'),
    path('acounts/signupview', views.SignUpView, name='signupview'),
   
]