from django.db import models

# Create your models here.
class SignUp(models.Model):
	email = models.EmailField();
	full_name = models.CharField(max_length=50, null=True, blank=False);
	# auto_now_add: Save timestamp upon creation
	# auto_now: Save when it is saved
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False);
	updated = models.DateTimeField(auto_now_add=False, auto_now=True);

	def __unicode__(self): # Python 3.3 uses __str__
		return self.email;