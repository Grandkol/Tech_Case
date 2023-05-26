from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms

from .models import Product

User = get_user_model()


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ("name",
                  "category",
                  "specifications",
                  "photo",
                  "price"
                  )
        labels = {
            "name": ("Название техники"),
            "category": ("Категория"),
        }
        help_text = {
            "specifications": ("Спецификации техники"),
        }


class CreationForm(UserCreationForm):
    password1 = forms.CharField(
        label="Пароль", widget=forms.PasswordInput(
            attrs={"class": "form-control"}
        )
    )
    password2 = forms.CharField(
        label="Подтверждение пароля",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
        }


class SignInForm(forms.Form):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            "username",
            "password1",
        )
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            # 'password1': forms.TextInput(attrs={'class': 'form-control'}),
        }
