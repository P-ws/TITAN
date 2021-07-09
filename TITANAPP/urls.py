from django.urls import path

from TITANAPP.views import TITAN_Introduce

app_name = 'TITANAPP'

urlpatterns = [
    path('introduce/', TITAN_Introduce, name='TITAN_Introduce'),
]