from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import get_user_model
from django import forms

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
         label= '아이디',
         widget=forms.TextInput(
            attrs={
                    'style' : 'border: 2px firebrick solid; border-radius: 10px; font-size: 20px;'
            }
         )
    )
    error_messages = {
         'password_mismatch': ("비밀번호가 일치하지 않습니다."),
    }
    password1 = forms.CharField(
         label='비밀번호',
         widget=forms.PasswordInput(
            attrs={
                    'style' : 'border: 2px firebrick solid; border-radius: 10px; font-size: 20px;'
            }
         )
    )
    password2 = forms.CharField(
         label='비밀번호 확인',
         widget=forms.PasswordInput(
            attrs={
                    'style' : 'border: 2px firebrick solid; border-radius: 10px; font-size: 20px;'
            }
         )
    ) 

    email = forms.CharField(
         label= '이메일',
         widget=forms.TextInput(
            attrs={
                    'style' : 'border: 2px firebrick solid; border-radius: 10px; font-size: 20px;'
            }
         )
    )
    first_name = forms.CharField(
         label= '이름',
         widget=forms.TextInput(
            attrs={
                    'style' : 'border: 2px firebrick solid; border-radius: 10px; font-size: 20px;'
            }
         )
    )
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
    
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code = 'password_mismatch',
            )
        return password2
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
        

class CustomUserChangeForm(UserChangeForm):

    email = forms.CharField(
         label= '이메일',
         widget=forms.TextInput(
            attrs={
                    'style' : 'border: 2px firebrick solid; border-radius: 10px; font-size: 20px;'
            }
        )
    )

    first_name = forms.CharField(
         label= '이름',
         widget=forms.TextInput(
            attrs={
                    'style' : 'border: 2px firebrick solid; border-radius: 10px; font-size: 20px;'
            }
         )
    )
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('email', 'first_name')

class CustomAuthenticationForm(AuthenticationForm):
        username = forms.CharField(
            label='아이디',
            widget=forms.TextInput(
                attrs={
                    'placeholder' : '  ID',
                    'style' : 'border: 2px firebrick solid; border-radius: 10px; font-size: 20px;'
            }
        )
    )
        password = forms.CharField(
            label='비밀번호',
            widget=forms.PasswordInput(
                attrs={
                    'placeholder' : '  PASSWORD',
                    'style' : 'border: 2px firebrick solid; border-radius: 10px; font-size: 20px;'
                }         
            )
        )

class CustomPasswordChangeForm(PasswordChangeForm):
    error_messages = {
         'password_mismatch': ("비밀번호가 일치하지 않습니다."),
    }

    old_password = forms.CharField(
         label='기존 비밀번호',
         widget=forms.PasswordInput(
            attrs={
                    'style' : 'border: 2px firebrick solid; border-radius: 10px; font-size: 20px;'
            }
         )
    )

    new_password1 = forms.CharField(
         label='새로운 비밀번호',
         widget=forms.PasswordInput(
            attrs={
                    'style' : 'border: 2px firebrick solid; border-radius: 10px; font-size: 20px;'
            }
         )
    )
    new_password2 = forms.CharField(
         label='비밀번호 확인',
         widget=forms.PasswordInput(
            attrs={
                    'style' : 'border: 2px firebrick solid; border-radius: 10px; font-size: 20px;'
            }
         )
    )

    # 기존 암호와 같을 경우
    def clean_new_password1(self):
        old_password = self.cleaned_data.get('old_password')
        new_password1 = self.cleaned_data.get('new_password1')

        if old_password and new_password1:
            if old_password == new_password1:
                raise forms.ValidationError('새로운 비밀번호는 기존 비밀번호와 다르게 입력해주세요')
        return new_password1
    
    # 새로운 암호가 서로 다를 경우
    def clean_new_password2(self):
        new_password1 = self.cleaned_data.get('new_password1')
        new_password2 = self.cleaned_data.get('new_password2')

        if new_password1 and new_password2 and new_password1 != new_password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code = 'password_mismatch',
            )
        return new_password2
    