from django import forms
from .models import Album

class AlbumForm(forms.ModelForm):
    content = forms.CharField(
        label='Title',
        widget=forms.TextInput(
        attrs= {
            'class' : 'form-control',
        }
        )
    )
    image = forms.ImageField(
        label = 'Image',
        widget = forms.ClearableFileInput(
            attrs= {
                'class': 'form-control',
            }
        ),
        required=False,
    )
    class Meta:
        model = Album
        fields = '__all__'
        