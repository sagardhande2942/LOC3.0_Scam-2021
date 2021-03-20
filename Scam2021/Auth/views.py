from django.shortcuts import render
from .models import *

def index(request):
    return render(request, 'Auth/index.html')

def register(request):
    if request.method == 'POST':
        demail = request.POST.get('email','')
        dcontact = request.POST.get('contact',1234567890)
        dfirstname = request.POST.get('fname','')
        dlastname = request.POST.get('lname','')
        dpass = request.POST.get('pass','')
        
        pdcheck = request.POST.get('pdcheck','false')
        if pdcheck == 'false':
            obj = Users.objects.create(email = demail, firstname = dfirstname, lastname = dlastname, contact = dcontact ,password = dpass)
            b = Patient.objects.create(user_id = obj)
        else:
            dspec = request.POST.get('spec','')
            obj = Users.objects.create(email = demail, firstname = dfirstname, contact = dcontact, lastname = dlastname, password = dpass)
            b = Doctor.objects.create(user_id = obj, d_qualif = dspec)
    return render(request, 'Auth/login.html')

def login(request):
    if request == 'POST':
        pdcheck = request.POST.get('pdcheck','false')
        if pdcheck == 'false':
            pemail = request.POST.get('email','')
            ppass = request.POST.get('pass','')
            p = Users.objects.filter(email = pemail)
            check = False
            if p.password == ppass:
                check = True
            
            if check == True:
                return render(request, '...')

        else:
            demail = request.POST.get('email','')
            dpass = request.POST.get('pass','')
            d = Users.objects.filter(email = demail)
            check = False
            if d.password == dpass:
                check = True
            if check == True:
                return render(request, '...')
