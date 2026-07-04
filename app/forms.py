from .models import *
from django.forms import ModelForm, TextInput, Textarea, Select, NumberInput

class TaskForm(ModelForm):
    class Meta:
        model = Task # Point Model which we are working with 
        fields = ["title", "task"]

        # Here we point atribudes for input frame
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter text'
            }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter content'
            }),
        }


# 1. create fields with Meta 
# 1.1 in the meta we piont the model which we are working with and fields
# 2. add widgets if you need 
# 2.1 in the widget we point type of the field add (attrs=) and atributes which you need


class WorkForm(ModelForm):
    class Meta:
        model = Work
        fields = ["name", "selery", "isHappy"]

        widgets = {
            "name": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter your work"
            }),

            "selery": NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Enter your selery"
            }),

            "isHappy": Select(attrs={
                "class": "form-control",
                "placeholder": "Enter your name"
            })
        }