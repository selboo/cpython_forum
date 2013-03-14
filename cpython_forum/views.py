#coding=utf-8
from django.http import HttpResponse
from django.contrib.auth.forms import *
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect
from cpython_forum.models import *

def index(request):
	topics      = Topic.objects.all()
	nodecates   = NodeCategory.objects.all()
	nodes	    = Node.objects.all()
	return render_to_response("index.html",{'name':request.user.username, 'topics':topics,\
            "nodecates":nodecates},context_instance=RequestContext(request))

def register(request):
	form = UserCreationForm()
	if request.method == 'GET':
		return render_to_response('register.html',{'form':form},context_instance=RequestContext(request))
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			new_user = form.save()
		return HttpResponseRedirect("/")
