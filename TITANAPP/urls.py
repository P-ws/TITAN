from django.contrib.auth.views import LoginView
from django.urls import path

from TITANAPP.views import TITAN_Introduce, TitanCreateView, AccountDetailView, AccountUpdateView, AccountDeleteView

app_name = 'TITANAPP'

urlpatterns = [
    path('introduce/', TITAN_Introduce, name='TITAN_Introduce'),
    path('create/', TitanCreateView.as_view(), name='create'),
    path('login/', LoginView.as_view(template_name='TITANAPP/login.html'), name='login'),
    path('logout/', LoginView.as_view(), name='logout'),
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),
    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'),
 ]