from django.forms import ModelForm
from django import forms
from .models import Testimonial


class TestimonialForm(ModelForm):
    class Meta:
        model = Testimonial
        fields = ['name', 'review', 'public', 'email']

    def __init__(self, *args, **kwargs):
        super(TestimonialForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'class': 'form-control',
             'placeholder': 'Enter your Name...'})
        self.fields['review'].widget.attrs.update(
            {'class': 'form-control',
             'placeholder': 'Enter your review...'})
