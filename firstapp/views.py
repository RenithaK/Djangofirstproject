from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.

from rest_framework.generics import GenericAPIView
from .serializers import MyclassSerializer
from .models import Myclass 

from rest_framework import status
class MyclassView(GenericAPIView):
    serializer_class=MyclassSerializer

    def post(self,request,*args,**kwargs):
        print(request.data)
        serializer=self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse("Saved successfully")
        else:
            return HttpResponse("Not saved")


    def get(self,*args,**kwargs):
        tabledata=Myclass.objects.all()
        Serializer=MyclassSerializer(tabledata,many=True)
        return JsonResponse(Serializer.data,safe=False)
        

