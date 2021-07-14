from django.urls import path

from TITANAPP.views import TITAN_Introduce, TitanCreateView

app_name = 'TITANAPP'

urlpatterns = [
    path('introduce/', TITAN_Introduce, name='TITAN_Introduce'),
    path('create/', TitanCreateView.as_view, name='create')
]