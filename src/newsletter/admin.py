from django.contrib import admin

# Register your models here.
from .models import SignUp

class SignUpAdmin(admin.ModelAdmin):
	# This changes how the signed up users show
	list_display = ["__unicode__", "timestamp", "updated"]
	class Meta:
		model = SignUp

admin.site.register(SignUp)