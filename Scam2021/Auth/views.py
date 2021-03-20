from django.shortcuts import render
from .models import *

def register(request):
    if request.method == 'POST':
        pdcheck = request.POST.get('pdcheck','false')
        if pdcheck == 'false':
            pemail = request.POST.get('email','')
            pcontact = request.POST.get('contact',1234567890)
            pfirstname = request.POST.get('fname','')
            plastname = request.POST.get('lname','')
            ppass = request.POST.get('pass','')
            obj = Users.objects.create(email = pemail, firstname = pfirstname, lastname = plastname, contact = pcontact ,password = ppass)
            b = Patient.objects.create(user_id = obj)
        else:
            demail = request.POST.get('email','')
            dcontact = request.POST.get('contact',1234567890)
            dfirstname = request.POST.get('fname','')
            dlastname = request.POST.get('lname','')
            dpass = request.POST.get('pass','')
            dspec = request.POST.get('spec','')
            obj = Users.objects.create(email = demail, firstname = dfirstname, contact = dcontact, lastname = dlastname, password = dpass, d_qualif = dspec)
            b = Doctor.objects.create(user_id = obj)
    return render(request, '')

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
