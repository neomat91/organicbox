# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def todoView(request):
	return HttpResponse('hello, this is a todoView')