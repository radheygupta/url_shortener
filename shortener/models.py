from django.db import models
from .utils import create_shortcode

class KirrManager(models.Manager):
	def all(self,*args,**kwargs):
		qs = super(KirrManager,self).all(*args,**kwargs)
		qs = qs.filter(active=True)
		return qs

	def refresh_shortcode(self):
		qs = KirrURL.objects.filter(id__gte=1)
		new_code_count = 0
		for q in qs:
			q.shortcode = create_shortcode(q)
			q.save()
			print(q.shortcode)
			new_code_count+=1
		return new_code_count	

class KirrURL(models.Model):
	url = models.CharField(max_length=220)
	shortcode = models.CharField(max_length=15, unique = True, blank=True)
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add=True)
	active = models.BooleanField(default=True)

	def __str__(self):
		return str(self.url)

	def save(self, *args, **kwargs):
		if self.shortcode is None or self.shortcode == "":
			self.shortcode = create_shortcode(self)
		super(KirrURL,self).save(*args, **kwargs)

	objects = KirrManager()	