from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import get_user_model
from django import forms


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
            label=False,
            widget=forms.TextInput(
            attrs = {
                'placeholder' : '아이디',
                'style' : 'width:200px;'
            }
            )
        )
    email = forms.EmailField(
            label=False,
            widget=forms.EmailInput(
            attrs = {
                'placeholder' : 'email 주소',
                'style' : 'width:200px;'
            }
            )
        )
    first_name = forms.CharField(
            label=False,
            widget=forms.TextInput(
            attrs = {
                'placeholder' : '성',
                'style' : 'width:200px;'
            }
            )
        )
    last_name = forms.CharField(
            label=False,
            widget=forms.TextInput(
            attrs = {
                'placeholder' : '이름',
                'style' : 'width:200px;'
            }
            )
        )
    
    birthday = forms.DateField(
        label= False,
        help_text='<br>생일을 입력해주세요',
        widget=forms.DateInput(
        attrs={
            'type': 'date',
            'style' : 'width:200px;'},
        ),
    )

    password1 = forms.CharField(
            label=False,
            widget=forms.PasswordInput(
            attrs = {
                'placeholder' : '비밀번호',
                'style' : 'width:200px;'
            }
            )
        )
    password2 = forms.CharField(
        label=False,
        widget=forms.PasswordInput(
            attrs = {
                'placeholder' : '비밀번호 확인',
                'style' : 'width:200px;'
            }
        )
    )
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'birthday', 'password1', 'password2')

class CustomUserChangeForm(UserChangeForm):
    email = forms.EmailField(
        label=False,
        widget=forms.EmailInput(
            attrs = {
                'placeholder' : 'email 주소'
            }
        )
    )
    first_name = forms.CharField(
        label=False,
        widget=forms.TextInput(
            attrs = {
                'placeholder' : '성'
            }
        )
    )
    last_name = forms.CharField(
        label=False,
        widget=forms.TextInput(
            attrs = {
                'placeholder' : '이름'
            }
        )
    )
    
    birthday = forms.DateField(
        label= False,
        help_text='<br>생일을 입력해주세요',
        widget=forms.DateInput(
            attrs={
                'type': 'date',
                'style' : 'width:180px;'
            },
        ),
    )
    password = None
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('email', 'birthday', 'first_name', 'last_name')

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label=False,
        widget=forms.TextInput(
            attrs = {
                'placeholder' : '아이디',
                'style' : 'width:200px;'
            }
        )
    )
    password = forms.CharField(
        label=False,
        widget=forms.PasswordInput(
            attrs = {
                'placeholder' : '비밀번호',
                'style' : 'width:200px;'
            }
        )
    )

class CustomPasswordChangeForm(PasswordChangeForm):
    new_password1 = forms.CharField(
        label='새 비밀번호',
        widget= forms.PasswordInput(),
        help_text='',
    )