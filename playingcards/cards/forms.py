from cards.models import Player

__author__ = 'CatsAir'
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class EmailUserCreationForm(UserCreationForm):
        email = forms.EmailField(required=True)
        first_name = forms.CharField(max_length=25)
        last_name = forms.CharField(max_length=25)
        phone_number = forms.CharField(max_length=20)

        class Meta:
            model = Player
            fields = ("first_name", "last_name", "username" ,"phone_number" ,"email" , "password1", "password2")

        def clean_username(self):
            # Since User.username is unique, this check is redundant,
            # but it sets a nicer error message than the ORM. See #13147.
            username = self.cleaned_data["username"]
            try:
                Player.objects.get(username=username)
            except Player.DoesNotExist:
                return username
            raise forms.ValidationError(
                self.error_messages['duplicate_username'],
                code='duplicate_username',
            )