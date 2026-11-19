from django.shortcuts import render,get_object_or_404

from rest_framework.generics import CreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from accounts.seriaizers import UserSerializer
from accounts.seriaizers import TrainerProfileSerializer,StudentProfileSerializer
from accounts.models import TrainerProfile,StudentProfile

from accounts.permissions import IsOwner

# Create your views here.

class SignUpView(CreateAPIView):

    serializer_class=UserSerializer

class TrainerRetriveUpdateDeleteView(RetrieveUpdateDestroyAPIView):

    permission_classes=[IsOwner]

    def get(self,request,pk=None):

        qs=get_object_or_404(TrainerProfile,id=pk)

        self.check_object_permissions(request,qs)

        serializer_instance=TrainerProfileSerializer(qs)

        return Response(data=serializer_instance.data)

    def put(self,request,pk=None):

        form_data=request.data

        trainer_object=get_object_or_404(TrainerProfile,id=pk)

        self.check_object_permissions(request,trainer_object)

        serializer_instance=TrainerProfileSerializer(data=form_data,instance=trainer_object)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data)

        else:

            return Response(data=serializer_instance.errors)

    def delete(self,request,pk=None):

        trainer_object=get_object_or_404(TrainerProfile,id=pk)

        self.check_object_permissions(request,trainer_object)

        TrainerProfile.objects.delete()

        response_data={"Message":"Deleted..."}

        return  Response(response_data)

class StudentRetriveUpdateDeleteView(RetrieveUpdateDestroyAPIView):

    queryset=StudentProfile.objects.all()

    serializer_class=StudentProfileSerializer  
