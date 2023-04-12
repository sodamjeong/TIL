from django import forms
from .models import Review, Comment


class ReviewForm(forms.ModelForm):
    movie = forms.CharField(
        label='영화 제목',
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
            } 
        )
    )
    title = forms.CharField(
        label='제목',
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
            } 
        )
    )
    content = forms.CharField(
        label='내용',
        widget = forms.Textarea(
            attrs = {
                'class': 'form-control',
                'rows': '5',
            }
        )
    )
    img_file = forms.ImageField(
        label = '이미지',
        widget = forms.ClearableFileInput(
            attrs= {
                'class': 'form-control',
            }
        ),
        required=False,
    )
    category = forms.CharField(
        label='카테고리',
        widget = forms.TextInput(
        attrs={
            'class': 'form-control',
            }
        )
    )
    class Meta:
        model = Review
        exclude = ('like_users', 'user',)

class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label= False,
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
                'style': 'width:100%',
            } 
        )
    )
    class Meta:
        model = Comment
        fields = ('content',)
