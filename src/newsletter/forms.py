from django import forms

from .models import SignUp

class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		# Specify which fields to show in order:
		fields = ['full_name', 'email']
		# exclude = ['full_name'] # use sparingly

	def clean_email(self): # Overriding the function for cleaning the email data
		email = self.cleaned_data.get('email')
		email_base, provider = email.split("@")
		domain, extension = provider.split('.')
		if not domain == 'USC':
			raise forms.ValidationError("Please use your USC email")
		if not extension == "edu":
			raise forms.ValidationError("Please use a valid .edu email address")
		return email

	def clean_full_name(self):
		full_name = self.cleaned_data.get('full_name')
		# write validation code
		return full_name