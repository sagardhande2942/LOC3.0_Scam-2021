import json
from django.http.response import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.shortcuts import render
from .Dis_Test import RFTest

d = RFTest()
dict1 = {}
def details(request):
    return render(request, 'details.html', dict1)

def index(request):
    
    gdict = {}
    b = d.get_dis()
    gdict = {
        'b': b
    }
    return render(request, 'indexsym.html', gdict)

def predictdis(request):
    b = request.POST.get('sym')
    global dict1
    dict1 = {}
    a = []
    str = ''
    for i in b:
        str += i
        if i == ' ':
            a.append(int(str))
            str = ''
    a.append(int(str))
        
    # print(a)
    # a = list(map(int, input().split()))
    x = len(a)
    for i in  range(x,17):
        a.append(0)
    print(a)
    
    result = d.RF_Predict(a)[0]
    dict1 = {
        'a':result,
    }
    print(result)
    return render(request, 'FindMyDoc.html', dict1)