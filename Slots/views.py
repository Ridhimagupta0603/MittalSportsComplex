from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from Sport.models import *
from django.contrib.auth.models import User
from .models import *
from .forms import *
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from datetime import datetime, date

# Create your views here.


def bookslots(request,sport):
    if request.user.is_authenticated:
        def numslots(user):
            return Bookslot.objects.filter(booked_by=user).count()



        if numslots(request.user)<3:
            booksport=Sport.objects.get(name=sport)
            slot=Bookslot()
            if request.method=='POST':
                bookform=Bookslotform(request.POST)
                if bookform.is_valid():
                    slot.booked_by=request.user
                    slot.sport=booksport
                    slot.court=Court.objects.get(id=request.POST['court'])
                    slot.slot=Timeslot.objects.get(id=request.POST['slot'])
                    slot.date=request.POST['date']
                    slot.save()
                    print('valid')
                    return redirect('sportpage')
            else:
                bookform=Bookslotform()

                return render(request,'Slots/bookslot.html',{'book_form':bookform})
    else:
        return redirect('user_login')


def slotlist(request):
    slots=Bookslot.objects.all()
    return render(request,'Slots/slots.html',{'slots':slots})
def cancelslot(request,id):
    
    b=Bookslot.objects.get(pk=id)
    print(b)
    b.delete()
    
    return redirect('sportpage')

