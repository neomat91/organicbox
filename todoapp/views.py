# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import TodoItem

# Create your views here.
def todoView(request):
	all_todo_items = TodoItem.objects.all()
	return render(request, 'todo.html',
		{'all_items': all_todo_items})

def addTodo(request):
	new_item = TodoItem(content = request.POST['content'])
	new_item.save()
	return HttpResponseRedirect('/todo/')
	# redirect the browser to '/todo/'