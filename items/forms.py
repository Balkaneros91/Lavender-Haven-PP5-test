from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(required=False, widget=CustomClearableFileInput)  # noqa

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        self.fields['image'].label = False
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'

    # def save(self, commit=True):
    #     instance = super().save(commit=False)
    #     instance.image = self.cleaned_data.get(
    #         'image')  # Set the Cloudinary image here
    #     if commit:
    #         instance.save()
    #     return instance
