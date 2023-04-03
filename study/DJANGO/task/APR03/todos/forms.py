from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    title = forms.CharField(
        label='Todo',
        widget=forms.TextInput(
            attrs={
                'class': 'my-title',
                'placeholder' : 'Title',
                'style' : 'border: 2px rgb(201, 186, 244) solid; border-radius: 10px;'
            },
        )
    )
    content = forms.CharField(
    label='Text',
    widget=forms.Textarea(
        attrs={
                'class': 'my-content',
                'placeholder' : 'story',
                'cols': '30', 'rows':'5',
                'style' : 'border: 2px rgb(201, 186, 244) solid; border-radius: 10px;'
        }, 
    )
)


    priority = forms.IntegerField(
        label='Importance',
    widget=forms.NumberInput(
        attrs={
                'min': 1, 'max': 10, 'value': 3,
                'style' : 'border: 2px rgb(201, 186, 244) solid; border-radius: 10px;'
        },
    )
)
    deadline = forms.DateField(
        label='D-day',
    widget=forms.DateInput(
        attrs={
                'type': 'date',
                'style' : 'border: 2px rgb(201, 186, 244) solid; border-radius: 10px;'
        },
    )
)

    class Meta:
        model = Todo
        fields = '__all__'