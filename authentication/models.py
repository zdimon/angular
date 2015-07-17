from django.db import models

from django.contrib.auth.models import AbstractBaseUser
from django.db import models


from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class AccountManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('Users must have a valid email address.')

        if not kwargs.get('username'):
            raise ValueError('Users must have a valid username.')

        account = self.model(
            email=self.normalize_email(email), username=kwargs.get('username')
        )

        account.set_password(password)
        account.save()

        return account

    def create_superuser(self, email, password, **kwargs):
        account = self.create_user(email, password, **kwargs)

        account.is_admin = True
        account.save()



class Account(User):
    about = models.CharField(max_length=40, blank=True)
    
    tagline = models.CharField(max_length=140, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #objects = AccountManager()

    #USERNAME_FIELD = 'email'
    #REQUIRED_FIELDS = ['username']

    def __unicode__(self):
        return self.email

    def get_full_name(self):
        return ' '.join([self.first_name, self.last_name])

    def get_short_name(self):
        return self.first_name


def create_custom_user(sender, instance, created, **kwargs):
    if created:
        values = {}
        for field in sender._meta.local_fields:
            values[field.attname] = getattr(instance, field.attname)
        user = Account(**values)
        user.save()

post_save.connect(create_custom_user, User)

