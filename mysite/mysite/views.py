from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt 
def login(request):
    if request.method == 'POST':
        #TODO: store it
        print("I revieved: " + eval(request.body)["password"])
        return HttpResponse("I revieved: " + eval(request.body)["password"])
    else:
        return HttpResponse("ERROR: This is a POST route")