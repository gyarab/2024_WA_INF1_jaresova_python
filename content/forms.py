from django import forms

class CommentForm(forms.Form):
    name = forms.CharField(label="Your name ",max_length=100)
    text = forms.CharField(label="Comment. ",widget=forms.Textarea)

class LoginForm(forms.Form):
    username = forms.CharField(label='Uživatelské jméno', max_length=100)
    password = forms.CharField(label='Heslo', widget=forms.PasswordInput)
