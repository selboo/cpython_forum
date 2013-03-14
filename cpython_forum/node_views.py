#coding=utf-8
from django.http import HttpResponse
from django.contrib.auth.forms import *
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect
from cpython_forum.models import *

def node_add (request):
	#topics      = Topic.objects.all()
	nodecates   = NodeCategory.objects.all()
	nodes	    = Node.objects.all()
	return render_to_response("node_add.html",{'name':request.user.username,'nodes':nodes,
            "nodecates":nodecates},context_instance=RequestContext(request))
