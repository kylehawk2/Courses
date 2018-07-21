# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from models import Course
from django.contrib import messages

def index(request):
    return render(request, 'courses/index.html', { "courses": Course.objects.all() })

def destroy(request, id):
    return render(request, 'courses/destroy.html', {"courses": Course.objects.get(id=int(id))})