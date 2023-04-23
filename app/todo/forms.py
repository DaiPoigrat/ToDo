from django.forms import ModelForm, TextInput, EmailInput, PasswordInput, Textarea, FileInput
from .models import Users, TodoList


class UserRegisterForm(ModelForm):
    class Meta:
        model = Users
        fields = ['username', 'mail', 'password']

        widgets = {
            'username': TextInput(attrs={
                'class': 'reg-form-input',
                'placeholder': 'username'
            }),
            'mail': EmailInput(attrs={
                'class': 'reg-form-input',
                'placeholder': 'email'
            }),
            'password': PasswordInput(attrs={
                'class': 'reg-form-input',
                'placeholder': 'password'
            })
        }


class UserAuthForm(ModelForm):
    class Meta:
        model = Users
        fields = ['mail', 'password']

        widgets = {
            'mail': EmailInput(attrs={
                'class': 'reg-form-input',
                'placeholder': 'email'
            }),
            'password': PasswordInput(attrs={
                'class': 'reg-form-input',
                'placeholder': 'password'
            })
        }


class AddTaskForm(ModelForm):
    class Meta:
        model = TodoList
        fields = ['name', 'text', 'passed']

        widgets = {
            'name': TextInput(attrs={
                'class': 'title-form-input',
                'placeholder': 'Title',
            }),
            'text': Textarea(attrs={
                'class': 'description-form-input',
                'placeholder': 'Description'
            })
        }


class UserUpdateForm(ModelForm):
    class Meta:
        model = Users
        fields = ['profile_photo', 'username']

        widgets = {
            'username': TextInput(attrs={
                'class': 'change-text-input',
                'placeholder': 'username'
            }),
            'profile_photo': FileInput(attrs={
                'class': 'profile-photo-input'
            })
        }
