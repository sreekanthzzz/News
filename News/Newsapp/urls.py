from django.urls import path, include

import Newsapp.views

urlpatterns = [

    path('', Newsapp.views.index, name='index'),
    path('Newsapp/Newspost/', Newsapp.views.Newspost, name='newspost'),
]