#coding=utf-8
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime   

class Node(models.Model):
	name         = models.CharField(max_length=30)
        nodecate_id  = models.IntegerField()
	date         = models.DateTimeField(auto_now_add=True, blank=True)	

class NodeCategory(models.Model):
	name         = models.CharField(max_length=30)
	description  = models.TextField()
	parent       = models.CharField(max_length=30)
		

class UserProfile(models.Model):
	user        = models.OneToOneField(User)
 	email       = models.CharField(max_length=120)
	description = models.TextField()
	website     = models.CharField(max_length=512)

class City(models.Model):
	name        = models.CharField(max_length=30)
	description = models.TextField()
	users       = models.ManyToManyField(UserProfile) 

class Reply(models.Model):
	topic_id  = models.IntegerField()
	author    = models.ManyToManyField(UserProfile)
	content   =  models.TextField()
	date      =  models.DateTimeField(auto_now_add=True, blank=True)	

class Topic(models.Model):
	author      =  models.ManyToManyField(UserProfile)	
	title       =  models.CharField(max_length=512)
	content     =  models.TextField()
        replys      =  models.ManyToManyField(Reply) 
	reply_count =  models.IntegerField()
	browse_count    = models.IntegerField()
	last_reply_date =  models.DateTimeField(auto_now_add=True, blank=True)	


class Notify(models.Model):
	topic_id  = models.IntegerField()
	author    = models.ManyToManyField(UserProfile)
	reply_id  = models.IntegerField()
	date      = models.DateTimeField(auto_now_add=True, blank=True)	
	
		
