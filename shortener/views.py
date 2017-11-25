from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import View

from .models import KirrURL

def kirr_FBV(request, shortcode=None, *args, **kwargs):
	obj = get_object_or_404(KirrURL, shortcode=shortcode)
	return HttpResponse("Hello! {sc}".format(sc=obj.url))

class kirr_CBV(View):	
	def get(self, request, shortcode=None, *args, **kwargs):
		obj = get_object_or_404(KirrURL, shortcode=shortcode)
		return HttpResponse("Hello again! {sc}".format(sc=obj.url))




