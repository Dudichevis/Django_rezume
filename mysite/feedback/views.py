from django.shortcuts import render, redirect
from .forms import FeedBackForm
from django.views.generic import View
from django.contrib import messages
from django.core.mail import send_mail



def post(request):
	if request.method == 'POST':
		form = FeedBackForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			phone = form.cleaned_data['phone']
			description = form.cleaned_data['description']

			mail = send_mail(name, email, 'igordudichev@gmail.com', ['monahmonah17@yandex.ru'],fail_silently=True)
			if mail:
				messages.success(request, 'Письмо отправлено')
				return redirect('/')
			else:
				messages.error(request, 'Ошибка отправки')
		else:
			messages.error(request, 'Ошибка регистрации')
	else:
		form = FeedBackForm()
	return render(request, 'webexample/contact.html', {"form" : form})


