# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from passlib.hash import pbkdf2_sha256


@csrf_exempt 
def login(request):
    if request.method == 'POST':
        if (request.body):
            data = json.loads(request.body)
            user = data["username"]
            password = data["password"]
            storedUsername = "Ethan"
            storedPassword = "Tuttle"
            encryptedStoredPassword = pbkdf2_sha256.hash(storedPassword)
            if (storedUsername == user and pbkdf2_sha256.verify(password, encryptedStoredPassword)):
                return JsonResponse({'isAuthenticated': True})
        return JsonResponse({'isAuthenticated': False})
    else:
        return HttpResponse("404: Route not available")


def id(request, key_id):
    if request.method == 'GET':
        return HttpResponse("Hello I am user {}".format(key_id))
    else:
        return HttpResponse("404: Route not available")
