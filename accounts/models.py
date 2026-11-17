from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):

    phone=models.CharField(max_length=15,unique=True)

    ROLE_CHOICES=(

        ('trainer','Trainer'),
        ('student','Student')
    )

    role=models.CharField(max_length=20,choices=ROLE_CHOICES,default="trainer")


class TrainerProfile(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='trainer_profile')

    qualification = models.CharField(max_length=150)

    specialization = models.CharField(max_length=150)

    experience = models.PositiveIntegerField(default=1)

    bio = models.TextField(blank=True, null=True)

    designation = models.CharField(max_length=100)

    def __str__(self):

        return self.user.username

class StudentProfile(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='student_profile')

    date_of_birth = models.DateField(null=True,blank=True)

    GENDER_CHOICES=(

        ('male','Male'),
        ('female','Female')
    )

    gender = models.CharField(max_length=20,choices=GENDER_CHOICES)

    education = models.CharField(max_length=150)

    college = models.CharField(max_length=150, blank=True)

    address = models.TextField(blank=True)

    guardian_name = models.CharField(max_length=150,blank=True)

    guardian_phone = models.CharField(max_length=15,blank=True)

    def __str__(self):

        return self.user.username
