from django.contrib.auth.models import (
    BaseUserManager,AbstractBaseUser
)
from django.db import models
from .choices import  DESIGNATION,GENDER,ROLE, TITLE
class MyUserManager(BaseUserManager):
    """create user using email as default field"""
    def create_user(self, email, password=None,active=True,staff=False,admin=False,**extra_fields):
        if not email:
            raise ValueError('provide an email address')
        user = self.model(email=self.normalize_email(email),
        **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,password):
        """create superuser """
        user= self.create_user(email,password)
        user.admin = True
        user.staff =True
        user.active = True
        user.superuser = True
        user.save(using=self._db)
        return user



class MyUser(AbstractBaseUser):
    """Myuser Model"""
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    first_name = models.CharField(verbose_name='Full Name', max_length=254)
    email = models.EmailField(verbose_name='email address', max_length=255,unique=True)
    surname = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=100,null=True)
    state = models.CharField(max_length=20)
    department = models.CharField(max_length=30, choices=DESIGNATION, blank=True,null=True)
    role = models.CharField(max_length=10,choices=ROLE, null=True)
    title= models.CharField(max_length=10,choices=TITLE,null=True)
    birth_date = models.DateField(null=True)
    years_of_practice = models.IntegerField(null=True)
    sex = models.CharField(max_length=8, choices=GENDER,null=True)
    timestamp = models.DateTimeField(auto_now=True)
    objects = MyUserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.first_name

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: AAll admins are staff
        return self.staff

    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        "Is the user active?"
        return self.active







