from django.shortcuts import render,get_object_or_404

from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from accounts.seriaizers import UserSerializer
from accounts.seriaizers import TrainerProfileSerializer,StudentProfileSerializer
from accounts.models import TrainerProfile,StudentProfile



# Create your views here.

class SignUpView(CreateAPIView):

    serializer_class=UserSerializer

class TrainerRetriveUpdateDeleteView(APIView):


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

        TrainerProfile.objects.filter(id=pk).delete()

        response_data={"Message":"Deleted..."}

        return  Response(response_data)

class StudentRetriveUpdateDeleteView(APIView):

    
    
    def get(self,request,pk=None):
    
        qs=get_object_or_404(StudentProfile,id=pk)
    
        self.check_object_permissions(request,qs)
    
        serializer_instance=StudentProfileSerializer(qs)
    
        return Response(data=serializer_instance.data)
    
    def put(self,request,pk=None):
    
        form_data=request.data
    
        student_object=get_object_or_404(TrainerProfile,id=pk)
    
        self.check_object_permissions(request,student_object)
    
        serializer_instance=StudentProfileSerializer(data=form_data,instance=student_object)
    
        if serializer_instance.is_valid():
    
            serializer_instance.save()
    
            return Response(data=serializer_instance.data)
    
        else:
    
            return Response(data=serializer_instance.errors)
    
    def delete(self,request,pk=None):
    
        student_object=get_object_or_404(StudentProfile,id=pk)
    
        self.check_object_permissions(request,student_object)
    
        StudentProfile.objects.filter(id=pk).delete()
    
        response_data={"Message":"Deleted..."}
    
        return  Response(response_data)

  
