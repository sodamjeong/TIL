from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
                'style': 'width:30%; border: 2px solid rgb(243, 230, 255);',
            } 
        )
    )
    content = forms.CharField(
        label='내용',
        widget = forms.Textarea(
            attrs = {
                'class': 'form-control',
                'style' : 'border: 2px solid rgb(243, 230, 255); width: 70%',
                'rows': '15',
                
            }
        )
    )
    category = forms.ChoiceField(
        label='카테고리',
        choices = Post.category_Choices,
        widget = forms.Select(
        attrs={
            'class': 'form-select',
            'style': 'height: 35px; border: 2px solid rgb(243, 230, 255); width: 100px'
            }
        )
    )
    img_file = forms.ImageField(
        label = '이미지 파일 선택',
        widget = forms.ClearableFileInput(
            attrs= {
                'class': 'form-control',
                'style': 'width: 70%; border: 2px solid rgb(243, 230, 255);'
            }
        ),
        required=False,
    )
    class Meta:
        model = Post
        exclude = ('like_users', 'user',)