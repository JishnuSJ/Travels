from django.shortcuts import render,redirect,HttpResponse
from django .http import HttpResponse
from .forms import BookingForm
from .models import Places,Doctors
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# Create your views here.
def hom(request):
    return render(request,'hom.html')
def index(request):
    dict_place={
        'places':Places.objects.all()
    }
    return render(request,'index.html',dict_place)

def about(request):
    return render(request,'about.html')
def booking(request):
    if request.method =="POST":                                #input user enter details to table 
        form =BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'conformation.html')
    form=BookingForm()                                        #display forms.py form in user view then goto booking.html
    dict_form={
        'form':form
    }

    return render(request,'booking.html',dict_form)
def doctors(request):
    dict_docs={
        'doctors':Doctors.objects.all()
    }
    return render(request,'package.html',dict_docs)                      
def contact(request):
    return render(request,'contact.html')
def places(request):
    dict_place={
        'places':Places.objects.all()
    }
    return render(request,'places.html',dict_place)

def loginn(request):
    if request.method == "POST":
        username=request.POST['username']
        password = request.POST['password']

        user =authenticate(username=username, password=password)


        if user is not None:
            login(request,user)
            return redirect('home')
        

        else:
            return redirect('signup')


    return render(request,'login.html')    



def signup(request):
    if request.method == "POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']

        myuser = User.objects.create_user(username=username, email=email, password=password)
        myuser.save()

        return redirect('login')
    
    return render(request,'signup.html')    