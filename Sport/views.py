from django.shortcuts import render,redirect


from Sport.models import*
from .models import *
from .forms import *
# Create your views here.
def sportpage(request):
    if request.user.is_superuser:
        return render(request,'Sport/sportpageadmin.html',{'sport':Sport.objects.all(),'court':Court.objects.all()})
    elif request.user.is_staff:
        return render(request,'Sport/sportpagestaff.html',{'sport':Sport.objects.all(),'court':Court.objects.all()})
    else :
        return render(request,'Sport/sportpagemem.html',{'sport':Sport.objects.all(),'court':Court.objects.all()})
def AddSport(request):
    if request.method=='POST':

        sport_form=AddSportForms(request.POST)
        if sport_form.is_valid():
           
            sport=sport_form.save()
            sport.save()
            return redirect('sportpage')
    else:
        sport_form=AddSportForms()
        
        return render(request,'Sport/Addsport.html',{'sport_form':sport_form})
def AddCourt(request):
    if request.method=='POST':

        court_form=AddCourtForms(request.POST)
        if court_form.is_valid():
           
            court=court_form.save()
            court.save()
            return redirect('sportpage')
    else:
        court_form=AddCourtForms()
        
        return render(request,'Sport/Addcourt.html',{'court_form':court_form})
def PerSportPage(request,sport):
    sport=Sport.objects.get(name=sport)
    
    return render(request,'Sport/PerSportPage.html',{'sport':sport})
def AddTimeslot(request):
    if request.method=='POST':

        Slot_form=AddTimeslotForms(request.POST)
        if Slot_form.is_valid():
           
            slot=Slot_form.save()
            slot.save()
            return redirect('sportpage')
    else:
        Slot_form=AddTimeslotForms()
        
        return render(request,'Sport/AddSlot.html',{'Slot_form':Slot_form})