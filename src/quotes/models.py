from django.db import models

# Create your models here.
class Quotes(models.Model):
	author =  models.CharField(max_length=50, blank=True, null=True)
	quote = models.CharField(max_length=500)

	def __unicode__(self): # Python 3 uses __str__
		return self.quote;