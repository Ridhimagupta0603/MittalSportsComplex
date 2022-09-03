from django.urls import path
from . import views


urlpatterns = [
    path('sportpage/',views.sportpage,name='sportpage' ),
    path('AddSport/',views.AddSport,name='AddSport' ),
    path('AddCourt/',views.AddCourt,name='AddCourt' ),
    path('AddSlots/',views.AddTimeslot,name='AddSlots' ),

    path('<str:sport>/',views.PerSportPage),
    



    

   


    
]