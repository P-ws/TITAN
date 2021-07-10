from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def TITAN_Introduce (requset):
    if requset.method == "POST":
        return render(requset, 'TITANAPP/middle.html',
                      context={'text':'POST METHOD!'})
    else:
        return render(requset, 'TITANAPP/middle.html',
                      context={'text':'GET METHOD!'})



