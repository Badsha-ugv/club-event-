from django.db import models

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=1000)
    desc = models.TextField(blank=True)
    date = models.CharField(max_length=100)
    venue = models.CharField(max_length=300)
    group = models.CharField(max_length=300,null=True,blank=True)
    duration = models.CharField(max_length=100)
    prize = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True) 


    def __str__(self):
        return self.title 


class EventRegister(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=100,blank=True)
    current_semester = models.CharField(max_length=100)
    event = models.ForeignKey(Event,on_delete=models.CASCADE)

    def __str__(self):
        return self.name 