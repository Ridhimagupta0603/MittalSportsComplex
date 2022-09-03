from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from Sport.models import *

# Create your models here.
class slot(models.Model):
    court=models.ForeignKey(Court,on_delete=models.CASCADE,null=True)
    slot=models.ForeignKey(Timeslot,on_delete=models.CASCADE,null=True)
    date=models.DateField(null=True)
    def __str__(self) -> str:
        return str(self.court)+'  '+str(self.slot)+'  '+str(self.date)

class Bookslot(models.Model):
    booked_by=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    sport=models.ForeignKey(Sport,on_delete=models.CASCADE,null=True)
    court=models.ForeignKey(Court,on_delete=models.CASCADE,null=True)
    slot=models.ForeignKey(Timeslot,on_delete=models.CASCADE,null=True)
    date=models.DateField(null=True)


   
    
  
    