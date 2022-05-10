from .models import Address
from django.forms import ModelForm, TextInput


class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = ['city', 'street', 'house', 'distance']

        widgets = {
            'city': TextInput(attrs={
                'class': 'field',
                'placeholder': 'Укажите город'
            }),
            'street': TextInput(attrs={
                'class': 'field',
                'placeholder': 'Укажите улицу'
            }),
            'house': TextInput(attrs={
                'class': 'field',
                'placeholder': 'Укажите дом'
            }),
            'distance': TextInput(attrs={
                'class': 'field',
                'placeholder': 'Укажите радиус (км)'
            })
        }
