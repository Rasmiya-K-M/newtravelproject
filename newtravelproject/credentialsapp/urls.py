
from django.urls import path

from . import views


urlpatterns = [


    path('registrations/',views.registrations,name='registrations'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]