from django.shortcuts import render
from .models import *
import mysql.connector

def index(request):
    return render(request, 'Auth/login.html')

def home(request):
    return render(request, 'Auth/home.html')


def findDoc(request):
    return render(request, 'Auth/FindMyDoc.html')

def chat(request):
    # mydb = mysql.connector.connect(
    # host="agri.cj9kv3v4akuv.us-east-2.rds.amazonaws.com",
    # user="inferno",
    # password="vishal2942",
    # database="chat"
    # )
    # mycursor = mydb.cursor()
    # a = request.body
    # b = a.decode("utf-8")

    # mycursor.execute('INSERT INTO chat values(%s, %s)', ('Sagar', b,))
    # mycursor.execute('SELECT msg FROM chat WHERE NAME = %s', ('Sagar'))
    # c = mycursor.fetchone()
    # dictt = {
    #     'c' : c
    # }
    return render(request, 'Auth/chat.html')

def booked(request):
    return render(request, 'Auth/booked.html')

def register(request):
    if request.method == 'POST':
        demail = request.POST.get('email','')
        dcontact = request.POST.get('contact',1234567890)
        dfirstname = request.POST.get('fname','')
        dlastname = request.POST.get('lname','')
        dpass = request.POST.get('pass','')
        
        pdcheck = request.POST.get('pdcheck','false')
        if pdcheck == 'false':
            obj = Users.objects.create(email = demail, first_name = dfirstname, last_name = dlastname, contact = dcontact ,password = dpass)
            b = Patient.objects.create(user_id = obj)
        else:
            dspec = request.POST.get('spec','')
            obj = Users.objects.create(email = demail, first_name = dfirstname, contact = dcontact, last_name = dlastname, password = dpass)
            b = Doctor.objects.create(user_id = obj, d_qualif = dspec)
    return render(request, 'Auth/Registration.html')

def login(request):
    # if request == 'POST':
    #     pdcheck = request.POST.get('pdcheck','false')
    #     if pdcheck == 'false':
    #         pemail = request.POST.get('email','')
    #         ppass = request.POST.get('pass','')
    #         p = Users.objects.filter(email = pemail)
    #         check = False
    #         if p.password == ppass:
    #             check = True
            
    #         if check == True:
    #             return render(request, 'login')

    #     else:
    #         demail = request.POST.get('email','')
    #         dpass = request.POST.get('pass','')
    #         d = Users.objects.filter(email = demail)
    #         check = False
    #         if d.password == dpass:
    #             check = True
    #         if check == True:

    if request.method == 'POST':
        pdcheck = request.POST.get('pdcheck','off')
        if pdcheck == 'on':
            return render(request,'Auth/doctors.html')
        
        else:
            return render(request, 'Auth/home.html')
