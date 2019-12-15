from django.forms import ModelForm, SelectDateWidget

from django.contrib.auth import get_user_model

from django.contrib.auth.forms import (
    AuthenticationForm, UserCreationForm
)

User = get_user_model()


class UserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = ('name', 'birthday', 'gender', 'email')
        MONTHS = {
            1: 'jan', 2: 'feb', 3: 'mar', 4: 'apr',
            5: 'may', 6: 'jun', 7: 'jul', 8: 'aug',
            9: 'sep', 10: 'oct', 11: 'nov', 12: 'dec'
        }
        widgets = {
            'birthday': SelectDateWidget(months=MONTHS, years=[x for x in range(19, 2030)])
        }


class LoginForm(AuthenticationForm):
    """ログインフォーム"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label  # placeholderにフィールドのラベルを入れる
