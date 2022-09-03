from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import ListView
from Sport.models import *
# Create your views here.

from django.shortcuts import redirect, render
from Users.forms import *
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

def user_login(request):
    if request.method == "POST":
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')

        user = authenticate(username=user_name, password=password)

        if user:
            
            if  user.is_superuser:
                login(request,user)
                return redirect('admin_home')    
            elif user.is_staff:
                login(request,user)
                return redirect('staff_home')   
             
            else:
                login(request,user)
                return redirect('member_home') 
           
        else:
            return HttpResponse("Please use correct id and password")
            

    else:
        return render(request, 'Users/login.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


# Create your views here.
def index(request):
    
   return render(request,'Users/homepage.html')


def register(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        

        if user_form.is_valid() :
            user = user_form.save()
            
            user.save()

            

            registered = True
       
    else:
        user_form = UserForm()
        

    return render(request, 'Users/registration.html',
                            {'registered':registered,
                             'user_form':user_form})

   
def staff_home(request):
    sport=Sport.objects.all()
    court=Court.objects.all()
    return render(request,'Users/staffpage.html',{'sport':sport,'court':court})
def member_home(request):
    sport=Sport.objects.all()
    court=Court.objects.all()
    return render(request,'Users/memberpage.html',{'sport':sport,'court':court})

def admin_home(request):
    sport=Sport.objects.all()
    court=Court.objects.all()
    return render(request,'Users/adminpage.html',{'sport':sport,'court':court})
def home(request):
    if request.user.is_authenticated:
        
        if  request.user.is_superuser:
                login(request,request.user)
                return redirect('admin_home')    
        elif request.user.is_staff:
            login(request,request.user)
            return redirect('staff_home')   
            
        else:
            login(request,request.user)
            return redirect('member_home')
    else:
        return redirect('index')
def Staffperm(request):
    if request.method=='POST':
        for user in User.objects.all():
            print(request.POST[user.username])
            if request.POST[user.username]=='False':
                user.is_staff=False
                user.save()
                print(user.is_staff,'member')
            elif request.POST[user.username]=='True' :
                user.is_staff=True
                user.save()
                print(user.is_staff, 'staff') 

        return redirect ('admin_home')
    else:

        return render(request,'Users/Staffperm.html',{'User':User.objects.all()})

class SearchView(ListView):
    model = Sport
    template_name = 'Users/search.html'
    context_object_name = 'all_search_results'

    def get_queryset(self):
        result = super(SearchView, self).get_queryset()
        query = self.request.GET.get('search')
        if query:
            postresult = Sport.objects.filter(name__contains=query)
            result = postresult
        else:
            result = None
        return result