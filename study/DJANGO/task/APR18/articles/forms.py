from django import forms
from .models import Article, Comment


class ArticleForm(forms.ModelForm):
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
    class Meta:
        model = Article
        exclude = ('like_users', 'user', 'emote_users')

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
