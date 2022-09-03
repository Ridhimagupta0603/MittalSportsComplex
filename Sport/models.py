from django.db import models

# Create your models here.

class Sport(models.Model):
    name=models.CharField(max_length=255)
    court=models.ManyToManyField('Court')
    slots=models.ManyToManyField('Timeslot')



    def __str__(self) -> str:
        return self.name
class Court(models.Model):
    court_name=models.CharField(max_length=255)
    capacity=models.IntegerField()
    def __str__(self) -> str:
        return self.court_name

class Timeslot(models.Model):
    fromtime=models.TimeField()
    totime=models.TimeField()
    def __str__(self) -> str:
        return str(self.fromtime)+ '  to   '   +str(self.totime)
