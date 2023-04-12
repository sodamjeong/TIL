from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import get_user_model
from django import forms

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
            label=False,
            widget=forms.TextInput(
            attrs = {
                'placeholder' : '아이디',
                'style' : 'width:100%;'
            }
            )
        )
    email = forms.EmailField(
            label=False,
            widget=forms.EmailInput(
            attrs = {
                'placeholder' : 'E-mail',
                'style' : 'width:100%;'
            }
            )
        )
    last_name = forms.CharField(
            label=False,
            widget=forms.TextInput(
            attrs = {
                'placeholder' : '이름',
                'style' : 'width:100%;'
            }
            )
        )
    birthday = forms.DateField(
        label= False,
        help_text='생일을 입력해주세요',
        widget=forms.DateInput(
        attrs={
            'type': 'date',
            'style' : 'width:100%;'
        }
        )
    )

    password1 = forms.CharField(
            label=False,
            widget=forms.PasswordInput(
            attrs = {
                'placeholder' : '비밀번호',
                'style' : 'width:100%;'
            }
            )
        )
    password2 = forms.CharField(
        label=False,
        widget=forms.PasswordInput(
            attrs = {
                'placeholder' : '비밀번호 확인',
                'style' : 'width:100%;'
            }
        )
    )
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'last_name', 'birthday', 'password1', 'password2')

class CustomUserChangeForm(UserChangeForm):
    email = forms.EmailField(
        label=False,
        widget=forms.EmailInput(
            attrs = {
                'placeholder' : 'E-mail',
                'style' : 'width:100%;'
            }
        )
    )
    last_name = forms.CharField(
        label=False,
        widget=forms.TextInput(
            attrs = {
                'placeholder' : '이름',
                'style' : 'width:100%;'
            }
        )
    )
    birthday = forms.DateField(
        label= False,
        help_text='생일을 입력해주세요',
        widget=forms.DateInput(
            attrs={
                'type': 'date',
                'style' : 'width:100%;'
            },
        ),
    )
    password = None
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('email', 'birthday', 'last_name')

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