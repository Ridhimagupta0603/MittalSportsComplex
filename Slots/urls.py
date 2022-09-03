from django.urls import path
from . import views


urlpatterns = [
    path('slotlist/',views.slotlist,name='slotlist' ),
    path('<str:sport>/',views.bookslots ),
    path('Cancel/<id>/',views.cancelslot),
    
   

  
   
    ]