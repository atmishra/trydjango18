from django.db import models

class newsletter(models.Model):
	email = models.EmailField()
	full_name = models.CharField(max_length=120,default='',blank=,null=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	update = models.DateTimeField(auto_now_add=False, auto_now=True)
