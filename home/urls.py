from django.urls import path,include
from .import views
urlpatterns = [
    path('',views.hom,name='hom'),
    path('home/',views.index,name='home'),   
    path('about/',views.about,name='about'),
    path('booking/',views.booking,name='booking'),
    path('doctors/',views.doctors,name='doctors'),
    path('contact/',views.contact,name='contact'),
    path('places/',views.places,name='places'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.loginn,name='login'),
    
]
