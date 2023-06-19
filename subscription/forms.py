from django.forms import ModelForm
from django import forms
from .models import Newsletter


class NewsletterForm(ModelForm):
    class Meta:
        model = Newsletter
        fields = ['email']

    def __init__(self, *args, **kwargs):
        super(NewsletterForm, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs.update(
            {'class': 'form-control',
             'placeholder': 'Enter your Email...'})
