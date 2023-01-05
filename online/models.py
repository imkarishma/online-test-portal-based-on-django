from tkinter import CASCADE
from turtle import mode
from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Question(models.Model):
    user=models.CharField(max_length=70)
    queno=models.IntegerField(primary_key=True,auto_created=True)
    question=models.CharField(max_length=200)
    optiona=models.CharField(max_length=100)
    optionb=models.CharField(max_length=100)
    optionc=models.CharField(max_length=100)
    optiond=models.CharField(max_length=100)
    answer=models.CharField(max_length=2)
    category=models.CharField(max_length=20)

class Detail(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    name=models.CharField(max_length=70)
    institute=models.CharField(max_length=100)
    degree=models.CharField(max_length=30)
    branch=models.CharField(max_length=20)
    image=models.ImageField(upload_to='images')
    points=models.IntegerField()
    solved=models.IntegerField()
    correct=models.IntegerField()
    worng=models.IntegerField()