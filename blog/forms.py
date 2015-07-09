from djangular.forms import NgModelFormMixin, NgModelForm
from .models import Comment
from djangular.styling.bootstrap3.forms import Bootstrap3Form
from django import forms

class CommentForm(Bootstrap3Form, NgModelFormMixin):
    author = forms.RegexField(r'^[A-Z][a-z -]?', label='Author',
        error_messages={'invalid': 'Author names shall start in upper case'})
    content = forms.CharField(label='Message',widget=forms.Textarea(attrs={'cols': 80, 'rows': 10}))
    post = forms.IntegerField(label='Message',widget=forms.HiddenInput()) 
