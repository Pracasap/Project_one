from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
	return render(request,'home.html', { })

def contact_view(request, *args, **kwargs):
	return render(request,'contact.html', {})

def about_view(request, *args, **kwargs):
	my_context = {
		'title': 'about page',
		'my_number': 123,
		'my_list': [1,2,3],
		'my_html': '<h1>Trying</h1>'
	}
	return render(request,'about.html', my_context)

def social_view(request, *args, **kwargs):
	return render(request,'home.html', {})