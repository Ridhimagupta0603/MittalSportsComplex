from django.urls import path
from Users import views


urlpatterns = [
    path('registration/',views.register,name='register' ),
    path('',views.index,name='index' ),
    path('home',views.home,name='home' ),


    path('login/',views.user_login,name='user_login' ),
    path('logout/',views.user_logout,name='user_logout' ),

    path('staff_home/',views.staff_home,name='staff_home' ),
    path('member_home/',views.member_home,name='member_home' ),
    path('ad',views.admin_home,name='admin_home' ),
    path('Staffperm',views.Staffperm,name='Staffperm' ),
     path('results/', views.SearchView.as_view(), name='search'),



    
]