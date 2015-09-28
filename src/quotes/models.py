from django.db import models

# Create your models here.
class Quote(models.Model):
	author =  models.CharField(max_length=50, blank=False, null=False)
	book = models.CharField(max_length=50, blank=True, null=True)
	passage = models.CharField(max_length=500, blank=False, null=False, primary_key=True)

	def __unicode__(self): # Python 3 uses __str__
		return self.passage