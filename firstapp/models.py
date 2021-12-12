from django.db import models

# Create your models here.


class Myclass(models.Model):
    Firstname=models.CharField(max_length=20)
    Lastname=models.CharField(max_length=20)
    Email=models.EmailField(unique=True)
    Phonenumber=models.IntegerField(null=False)

    def __str__(self):
        return self.Firstname