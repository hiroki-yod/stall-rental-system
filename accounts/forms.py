from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from .models import User


class CustomFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            # 認証関連のフォームの共通スタイリング
            field.widget.attrs.update({
                'class': 'block w-full rounded-md border-0 px-3 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300',
            })


class SignUpForm(CustomFormMixin, UserCreationForm):
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=16)
    
    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number:
            if not phone_number.isdigit() or len(phone_number) not in [10, 11]:
                raise ValidationError('電話番号は10桁または11桁の数字で入力してください。')
        return phone_number

    class Meta:
        model = User
        fields = ("username", "email", "phone_number", "password1", "password2")


class LoginForm(CustomFormMixin, AuthenticationForm):
    pass
