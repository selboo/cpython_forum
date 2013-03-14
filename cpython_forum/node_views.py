#coding=utf-8
from django.http import HttpResponse
from django.contrib.auth.forms import *
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect
from cpython_forum.models import *
from cpython_forum.forms import *

def nodecate_add (request):
	nodecates   = NodeCategory.objects.all()
	return render_to_response("nodecate_add.html",{'name':request.user.username,
            "nodecates":nodecates},context_instance=RequestContext(request))

def nodecate_save(request):

	if request.method == 'POST':
		nodecate = NodeCategory(name=request.POST['name'],description=request.POST['description'])
		nodecate.save()
		return  HttpResponseRedirect('/')		
