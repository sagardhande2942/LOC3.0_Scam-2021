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
            obj = Users(email = pemail, firstname = pfirstname, lastname = plastname, contact = pcontact ,password = ppass)
            a = Users.objects.get(id = obj.id)
            b = Patient(p_id = a)
            obj.save()
        else:
            demail = request.POST.get('email','')
            dcontact = request.POST.get('contact',1234567890)
            dfirstname = request.POST.get('fname','')
            dlastname = request.POST.get('lname','')
            dpass = request.POST.get('pass','')
            dspec = request.POST.get('spec','')
            obj = Users(email = demail, firstname = dfirstname, contact = dcontact, lastname = dlastname, password = dpass, d_qualif = dspec)
            a = Users.objects.get(id = obj.id)
            b = Patient(p_id = a)
            obj.save()
    return render(request, '')

def login(request):
    if request == 'POST':
        pdcheck = request.POST.get('pdcheck','false')
        if pdcheck == 'false':
            pemail = request.POST.get('email','')
            ppass = request.POST.get('pass','')
            pset = Users.objects.all()
            check = False
            for i in pset.iterator():
                if i.email == pemail and i.password == ppass:
                    check = True
            
            if check == True:
                return render(request, '...')

        else:
            demail = request.POST.get('email','')
            dpass = request.POST.get('pass','')
            dset = Users.objects.all()
            check = False
            for i in dset.iterator():
                if i.email == demail and i.password == dpass:
                    check = True
            if check == True:
                return render(request, '...')
