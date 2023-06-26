# from django.forms import ModelForm
# from django import forms
# from .models import Review


# class ReviewForm(forms.ModelForm):
#     class Meta:
#         model = Review
#         fields = ['name', 'email', 'review']

#         widgets = {
#             'name': forms.TextInput(attrs={'placeholder': 'Enter your name',
#                                     'required': True}),
#             'email': forms.EmailInput
#             (attrs={'placeholder': 'Enter your email'}),
#             'review': forms.Textarea
#             (attrs={'rows': 2, 'placeholder': 'Type here your testimonial'}),
#         }

#         # def __init__(self, *args, **kwargs):
#         #     super(ReviewForm, self).__init__(*args, **kwargs)
#         #     self.fields['name'].widget.attrs.update(
#         #         {'class': 'form-control',
#         #          'placeholder': 'Enter your Name...'})
#         #     self.fields['review'].widget.attrs.update(
#         #         {'class': 'form-control',
#         #          'placeholder': 'Enter your review...'})
