from django import forms
from .models import Tours


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    tour_name = forms.CharField(max_length=200)
    address = forms.CharField(max_length=255)
    email = forms.EmailField()
    phone = forms.IntegerField()
    message = forms.CharField(widget=forms.Textarea)
