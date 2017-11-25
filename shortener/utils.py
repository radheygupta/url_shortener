from django.conf import settings
import random
import string

SHORTCODE_MIN = getattr(settings, "SHORTCODE_MIN", 5)

def code_generator(size=SHORTCODE_MIN, chars=string.ascii_lowercase + string.digits):
	return ''.join([random.choice(chars) for _ in range(size)])

def create_shortcode(instance,size=SHORTCODE_MIN):
	new_code = code_generator(size=size)
	Kirr = instance.__class__
	is_exists = Kirr.objects.filter(shortcode=new_code).exists()
	if is_exists:
		return create_shortcode(instance,size)
	else:
		return new_code	
