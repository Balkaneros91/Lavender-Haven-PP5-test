from django.forms import ModelForm
from django import forms
from .models import ContactMessage


class ContactMessageForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message_subject', 'message']

    def __init__(self, *args, **kwargs):
        super(ContactMessageForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'class': 'form-control',
             'placeholder': 'Enter your Name...'})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control',
             'placeholder': 'Enter your Email...'})
        self.fields['message_subject'].widget.attrs.update(
            {'class': 'form-control',
             'placeholder': 'Name the messages subject...'})
        self.fields['message'].widget.attrs.update(
            {'class': 'form-control',
             'placeholder': 'Enter your Message...'})


# class ContactForm(forms.ModelForm):
#     """
#     Form class for the contact form
#     """
#     class Meta:
#         model = ContactMessage
#         fields = '__all__'

#     def __init__(self, *args, **kwargs):
#         """
#         Add placeholders and remove auto-generated
#         labels
#         """
#         super().__init__(*args, **kwargs)

#         placeholders = {
#             'name': 'Enter your name and surname',
#             'email': 'Enter your email address',
#             'question_categories': 'Name the purpose/subject',
#             'message': 'Your Message',
#         }

#         self.fields['email'].widget.attrs['autofocus'] = True
#         for field in self.fields:
#             if field != 'message':
#                 if self.fields[field].required:
#                     placeholder = f'{placeholders[field]} *'
#                 else:
#                     placeholder = placeholders[field]
#                 self.fields[field].widget.attrs['placeholder'] = placeholder
#             self.fields[field].widget.attrs['class'] = 'border-black rounded-0 profile-form-input'   # noqa
#             self.fields[field].label = False
