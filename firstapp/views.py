from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from rest_framework.generics import GenericAPIView
from .serializers import MyclassSerializer

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