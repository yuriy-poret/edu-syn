from django import forms
from .models import UserName


class NameForm(forms.ModelForm):
    class Meta:
        model = UserName
        fields = ['name']
        labels = {'name': 'Ваше имя'}
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Введите имя'
            })
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name or name.strip() == '':
            raise forms.ValidationError("Имя не может быть пустым!")
        return name.strip()
