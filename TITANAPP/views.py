from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from TITANAPP.models import NewModel


def TITAN_Introduce (requset):
    if requset.method == "POST":
        temp = requset.POST.get('input_text')
        model_instance = NewModel()
        model_instance.text = temp
        model_instance.save()

        data_list = NewModel.objects.all()
        return render(requset, 'TITANAPP/middle.html',
                      context={'data_list': data_list})
    else:
        data_list = NewModel.objects.all()
        return render(requset, 'TITANAPP/middle.html',
                      context={'data_list': data_list})



