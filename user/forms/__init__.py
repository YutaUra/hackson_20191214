from django.forms import ModelForm, SelectDateWidget

from django.contrib.auth import get_user_model

from django.contrib.auth.forms import (
    AuthenticationForm
)

User = get_user_model()


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = (
            'name',
            'birthday',
            'gender',
            'email',
            'password',
        )
        MONTHS = {
            1: 'jan', 2: 'feb', 3: 'mar', 4: 'apr',
            5: 'may', 6: 'jun', 7: 'jul', 8: 'aug',
            9: 'sep', 10: 'oct', 11: 'nov', 12: 'dec'
        }
        widgets = {
            'birthday': SelectDateWidget(months=MONTHS, years=[x for x in range(1900, 2030)])
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        User.objects.filter(email=email, is_active=False).delete()
        return email


class LoginForm(AuthenticationForm):
    """ログインフォーム"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label  # placeholderにフィールドのラベルを入れる
