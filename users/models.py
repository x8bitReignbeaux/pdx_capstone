from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.
class Ethnicity(models.Model):
    ethnicity = models.CharField(max_length=25)
    isActive = models.BooleanField(default=True)
    
    def __str__(self):
        return self.ethnicity
    
class GenderIdentity(models.Model):
    gender_identity = models.CharField(max_length=25)
    isActive = models.BooleanField(default=True)
    
    def __str__(self):
        return self.gender_identity
    
class SexualOrientation(models.Model):
    sexual_orientation = models.CharField(max_length=25)
    isActive = models.BooleanField(default=True)
    
    def __str__(self):
        return self.sexual_orientation
    
class UserProfile(AbstractUser):
    date_of_birth = models.DateField(null=True)
    ethnicity = models.ForeignKey('Ethnicity', on_delete=models.SET_NULL, null=True)
    gender_identity = models.ForeignKey('GenderIdentity', on_delete=models.SET_NULL, null=True)
    sexual_orientation = models.ForeignKey('SexualOrientation', on_delete=models.SET_NULL, null=True)
    is_admin = models.BooleanField(default=False) 
    
    #def __str__(self):
    #    return user.username
    

#class MyUserManager(BaseUserManager):
#    def create_user(self, email, date_of_birth, password=None):
#        """
#        Creates and saves a User with the given email, date of
#        birth and password.
#        """
#        if not email:
#            raise ValueError('Users must have an email address')

#        user = self.model(
#            email=self.normalize_email(email),
#            date_of_birth=date_of_birth,
#        )

#        user.set_password(password)
#        user.save(using=self._db)
#        return user

#    def create_superuser(self, email, date_of_birth, password=None):
#        """
#        Creates and saves a superuser with the given email, date of
#        birth and password.
#        """
#        user = self.create_user(
#            email,
#            password=password,
#            date_of_birth=date_of_birth,
#        )
#        user.is_admin = True
#        user.save(using=self._db)
#        return user


#class MyUser(AbstractBaseUser):
#    email = models.EmailField(
#        verbose_name='email address',
#        max_length=255,
#        unique=True,
#    )
#    date_of_birth = models.DateField()
#    is_active = models.BooleanField(default=True)
#    is_admin = models.BooleanField(default=False)

#    objects = MyUserManager()

#    USERNAME_FIELD = 'email'
#    REQUIRED_FIELDS = ['date_of_birth']

#    def __str__(self):
#        return self.email

#    def has_perm(self, perm, obj=None):
#        "Does the user have a specific permission?"
#        # Simplest possible answer: Yes, always
#        return True

#    def has_module_perms(self, app_label):
#        "Does the user have permissions to view the app `app_label`?"
#        # Simplest possible answer: Yes, always
#        return True

#    @property
#    def is_staff(self):
#        "Is the user a member of staff?"
#        # Simplest possible answer: All admins are staff
#        return self.is_admin