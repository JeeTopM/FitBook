from django import forms
from .models import Exercise


class ExerciseForm(forms.ModelForm):
    """Форма для добавления упражнения"""

    class Meta:
        model = Exercise
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Например: Подтягивания'
            })
        }
        labels = {
            'name': 'Название упражнения'
        }

    def clean_name(self):
        """Очистка названия - первая буква заглавная"""
        name = self.cleaned_data['name'].strip()
        if name:
            name = name[0].upper() + name[1:].lower()
        return name