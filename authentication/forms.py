from djangular.forms import NgModelFormMixin, NgModelForm, NgFormValidationMixin
from .models import Account
from djangular.styling.bootstrap3.forms import Bootstrap3Form
from django import forms

class AccountForm(NgModelFormMixin, NgModelForm):
    
    class Meta:
        model = Account
        fields = ('email','username')
         
