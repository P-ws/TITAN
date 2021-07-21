from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from TITANAPP.forms import AccountCreationForm
from TITANAPP.models import NewModel


@login_required
def TITAN_Introduce (request):
    if request.method == "POST":
        temp = request.POST.get('input_text')
        model_instance = NewModel()
        model_instance.text = temp
        model_instance.save()

        return HttpResponseRedirect(reverse('TITANAPP:TITAN_Introduce'))

    else:
        data_list = NewModel.objects.all()
        return render(request, 'TITANAPP/middle.html',
                      context={'data_list': data_list})



class TitanCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    # lazy 붙인이유: 바로나오는게 아니라 불러와줄때만 사용하기 위해
    success_url = reverse_lazy('TITANAPP:TITAN_Introduce')
    template_name = 'TITANAPP/create.html'


class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'TITANAPP/detail.html'


@method_decorator(login_required, 'post')
@method_decorator(login_required, 'get')
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountCreationForm
    context_object_name = 'target_user'
    success_url = reverse_lazy('TITANAPP:TITAN_Introduce')
    template_name = 'TITANAPP/update.html'


@method_decorator(login_required, 'post')
@method_decorator(login_required, 'get')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('TITANAPP:TITAN_Introduce')
    template_name = 'TITANAPP/delete.html'

