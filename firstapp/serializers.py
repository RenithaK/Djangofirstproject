from rest_framework import serializers
from .models import Myclass


class MyclassSerializer(serializers.ModelSerializer):
    class Meta:
        model=Myclass
        fields=['Firstname','Lastname','Email','Phonenumber']