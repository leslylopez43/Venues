
from django.urls import path
from . import views 


urlpatterns = [
    path('app11/', 
    views.members, 
    name='app11_function'),
]
