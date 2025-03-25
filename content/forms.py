from django import forms

class CommentForm(forms.Form):
    name = forms.CharField(label="Your name ",max_length=100)
    text = forms.CharField(label="Comment. ",widget=forms.Textarea)