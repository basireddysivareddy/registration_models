from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *
# Create your views here.
from django.core.mail import send_mail
def home(request):
    return render(request,'home.html')
def registration(request):
    uf=UserForm()
    pf=ProfileForm()
    d={'uf':uf,'pf':pf}
    if request.method=='POST' and request.FILES:
        UD=UserForm(request.POST)
        PD=ProfileForm(request.POST,request.FILES)
        if UD.is_valid() and PD.is_valid():
            PW=UD.cleaned_data['password']
            USO=UD.save(commit=False)
            USO.set_password(PW)
            USO.save()

            PFO=PD.save(commit=False)
            PFO.User=USO
            PFO.save()

            send_mail('User registration',
            'Registration is successfully',
            'basireddysivareddy45848@gmail.com',
            [USO.email],fail_silently=False)
            return HttpResponse('Registration is successfully')

        
    return render(request,'registration.html',d)