from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Field
from.models import MyUser





class MedicalCreationForm(forms.ModelForm):
    """A form for creating new medical user """
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ('title','first_name', 'surname',  'years_of_practice',
                         'sex', 'department', 'email', 'role','birth_date', 'phone','state','address')
        widgets = {
            'birth_date': forms.DateTimeInput(format=("%Y-%m-%d"), attrs={'class': 'form-control',  'type': 'date'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter First Name'}),
            'surname': forms.TextInput(attrs={'placeholder': 'Enter Surname'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter Email'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Enter Phone Number'}),
            'role': forms.Select(),
        }
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(

                Column('title', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('first_name', css_class='form-group col-md-6 mb-0'),
                Column('surname', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('password1', css_class='form-group col-md-6 mb-0'),
                Column('password2', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(

                Column('email', css_class='form-group col-md-6 mb-0'),
                Column('phone', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('address', css_class='form-group col-md-6 mb-0'),
                Column('state', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('birth_date', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),

            Row(
                Column('role', css_class='form-group col-md-6 mb-0'),
                Column('department', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('years_of_practice', css_class='form-group col-md-6 mb-0'),
                Column('sex', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),

        )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = MyUser.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is taken")
        return email

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class PatientCreationForm(forms.ModelForm):
    """A form for creating new patient user"""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ('title','first_name', 'surname',
                         'sex', 'email', 'role','birth_date', 'phone','state','address')
      

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(

                Column('title', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('first_name', css_class='form-group col-md-6 mb-0'),
                Column('surname', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('password1', css_class='form-group col-md-6 mb-0'),
                Column('password2', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(

                Column('email', css_class='form-group col-md-6 mb-0'),
                Column('phone', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('address', css_class='form-group col-md-6 mb-0'),
                Column('state', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('birth_date', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),

            Row(
                Column('role', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('sex', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),

        )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = MyUser.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is taken")
        return email

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = MyUser
        fields = ('email', 'password', 'first_name',
                  'admin', 'active')

    def clean_password(self):
        return self.initial["password"]


