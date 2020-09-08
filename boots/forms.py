from django import forms
from .widgets import CustomClearableFileInput
from .models import Boot, Brand


class ProductForm(forms.ModelForm):

    class Meta:
        model = Boot
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        brands = Brand.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in brands]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
