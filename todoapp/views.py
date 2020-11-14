# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from .models import TodoItem

# Create your views here.
def todoView(request):
	all_todo_items = TodoItem.objects.all()
	return render(request, 'todo.html',
		{'all_items': all_todo_items})