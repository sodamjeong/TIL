from django import forms
from .models import Diary

class DiaryForm(forms.ModelForm):
    title = forms.CharField(
        label='Title',
        widget=forms.TextInput(
            attrs={
                'placeholder' : '  제목',
                'style' : 'border: 2px rgb(201, 186, 244) solid; border-radius: 10px;'
            },
        )
    )

    record_date = forms.DateField(
        label='Date.',
    widget=forms.DateInput(
        attrs={
                'type': 'date',
                'style' : 'border: 2px rgb(201, 186, 244) solid; border-radius: 10px;'
        },
    )
)
    content = forms.CharField(
    label='Text',
    widget=forms.Textarea(
        attrs={
                'placeholder' : '  내용',
                'cols': '30', 'rows':'5',
                'style' : 'border: 2px rgb(201, 186, 244) solid; border-radius: 10px;'
        }, 
    )
)

    class Meta:
        model = Diary
        fields = '__all__'