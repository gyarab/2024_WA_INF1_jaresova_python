from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Field

class CommentForm(forms.Form):
    name = forms.CharField(label="Your name ",max_length=100, required=False)
    text = forms.CharField(label="Comment ",widget=forms.Textarea)

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

class LogoutForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Submit('submit', 'Logout', css_class='btn-primary')
        )     

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    password1 = forms.CharField(label="Password",widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(label="Password again", widget=forms.PasswordInput, required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Field('username'),
                Field('password1'),
                Field('password2'),
            ),            
            Submit('submit', 'Create an account', css_class='btn-primary')
        )