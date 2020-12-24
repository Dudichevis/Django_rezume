
from django.forms import ModelForm, TextInput
from django import forms

class FeedBackForm(forms.Form):
	name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class' : 'form-control'}))
	email = forms.CharField(label='Почта', widget=forms.TextInput(attrs={'class' : 'form-control'}))
	phone = forms.CharField(label='Телефон', widget=forms.TextInput(attrs={'class' : 'form-control'}))
	description = forms.CharField(label='Добавить сообщение...', widget=forms.Textarea(attrs={'class' : 'form-control'}))