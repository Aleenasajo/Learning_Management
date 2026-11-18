from django.shortcuts import render

from rest_framework.generics import CreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from accounts.seriaizers import UserSerializer
from accounts.seriaizers import TrainerProfileSerializer,StudentProfileSerializer
from accounts.models import TrainerProfile,StudentProfile

# Create your views here.

class SignUpView(CreateAPIView):

    serializer_class=UserSerializer

class TrainerRetriveUpdateDeleteView(RetrieveUpdateDestroyAPIView):

    queryset=TrainerProfile.objects.all()

    serializer_class=TrainerProfileSerializer

class StudentRetriveUpdateDeleteView(RetrieveUpdateDestroyAPIView):

    queryset=StudentProfile.objects.all()

    serializer_class=StudentProfileSerializer  
