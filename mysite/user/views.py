# -*- coding: utf-8 -*-
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
        return HttpResponse("404: Route not available")


def id(request, key_id):
    if request.method == 'GET':
        return HttpResponse("Hello I am user {}".format(key_id))
    else:
        return HttpResponse("404: Route not available")
