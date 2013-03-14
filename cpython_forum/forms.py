#coding=utf-8

from django import forms

class NodeCateForm(forms.Form):
	name          = forms.CharField()
	description   = forms.CharField(widget=forms.Textarea ) 
