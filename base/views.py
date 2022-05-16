import re
from django.http import HttpResponse
from django.shortcuts import render


rooms =[ 
        {'id':1, 'name':'Lets Learn Python!'},
        {'id':2, 'name':'Lets Learn JavaScript!'},
        {'id':3, 'name':'Lets Learn Django!'},
       ]

# Create your views here.
def home(request):
    context = {'rooms':rooms}
    return render (request, 'base/home.html', context)

def room(request,pk):
    return render (request, 'base/room.html')