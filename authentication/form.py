# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# start tutorial
from django import forms
from django.core.exceptions import ValidationError
from djangular.styling.bootstrap3.forms import Bootstrap3Form
from djangular.forms import NgModelFormMixin, NgModelForm


def validate_password(value):
    # Just for demo. Do not validate passwords like this!
    if value != 'secret':
        raise ValidationError('The password is wrong.')


class AuthForm(Bootstrap3Form, NgModelFormMixin):
    username = forms.RegexField(r'^[A-Z][a-z -]?', label='Last name',
        error_messages={'invalid': 'Last names shall start in upper case'})
    password = forms.CharField(label='Password', widget=forms.PasswordInput,
        validators=[validate_password],
        help_text='The password is "secret"')
