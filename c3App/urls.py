from django.urls import path, include
from .views import home, reports


urlpatterns = [

    path('', home, name='home'),
    path('reports/', reports, name='reports'),

]