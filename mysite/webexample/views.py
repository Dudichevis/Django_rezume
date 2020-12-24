from django.shortcuts import render, redirect
from django.views.generic import DetailView


def index(request):
	return render(request, 'webexample/index.html', {'title': 'Главная страница'})

def rezume(request):
	return render(request, 'webexample/rezume.html')

def contact(request):
	return render(request, 'webexample/contact.html')

def create(request):
	form = ContactsForm()

	data = {
		'form' : form
	}
	return render(request, 'webexample/contact.html')
