from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
	title		= forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Your title'}))
	email 		= forms.EmailField()
	description	= forms.CharField(
						required=False, 
						widget=forms.Textarea(
								attrs={
									'placeholder': 'Description',
									'class': 'new-class-name two',
									'rows': 20,
									'cols': 60
								}
							)
						)
	price		= forms.DecimalField(initial=29.99)
	class Meta:
		model = Product
		fields = [
			'title',
			'description',
			'price'
		]

	def clean_title(self, *args, **kwargs):
		title = self.cleaned_data.get('title')
		if 'p' in title:
			return title
		else:
			raise forms.ValidationError('This is not a valid title')

	def clean_email(self, *args, **kwargs):
		email = self.cleaned_data.get('email')
		if not email.endswith('com'):
			raise forms.ValidationError('Invalid Email')
			return email


class RawProductForm(forms.Form):
	title		= forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Your title'}))
	description	= forms.CharField(
						required=False, 
						widget=forms.Textarea(
								attrs={
									'placeholder': 'Description',
									'class': 'new-class-name two',
									'rows': 20,
									'cols': 60
								}
							)
						)
	price		= forms.DecimalField(initial=29.99)
