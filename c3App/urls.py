from django.urls import path, include
from .views import homeTemplateView


urlpatterns = [

    path('',homeTemplateView.as_view, name='home'),
    #path('reports/', reports, name='reports'),

]