from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm, UserModel
from django.contrib.auth import password_validation
from django.forms import inlineformset_factory

class UserRegistrationForm(UserCreationForm):
    email = None
    password = None

    class Meta:
        model = UserModel
        fields = ("username","password")

class AddPoll(forms.ModelForm):
    class Meta:
        model = models.Question
        fields = ['question_text','pub_date']

class AddChoice(forms.ModelForm):
    class Meta:
        model = models.Choice
        fields = ['choice_text']

QuestionMetaInlineFormset = inlineformset_factory(
    models.Question,
    models.Choice,
    form=AddChoice,
    extra=3,
    # max_num=5,
    # fk_name=None,
    # fields=None, exclude=None, can_order=False,
    # can_delete=True, max_num=None, formfield_callback=None,
    # widgets=None, validate_max=False, localized_fields=None,
    # labels=None, help_texts=None, error_messages=None,
    # min_num=None, validate_min=False, field_classes=None
)