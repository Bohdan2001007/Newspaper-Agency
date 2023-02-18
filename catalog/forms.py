from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from catalog.models import Redactor, Newspaper


class RedactorCreateForm(forms.ModelForm):

    class Meta:
        model = Redactor
        fields = UserCreationForm.Meta.fields + (
            "password", "first_name", "last_name", "years_of_experience"
        )


class RedactorExperienceUpdateForm(forms.ModelForm):

    class Meta:
        model = Redactor
        fields = ("years_of_experience",)


class NewspaperForm(forms.ModelForm):
    redactors = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Newspaper
        fields = "__all__"


class NewspaperSearchForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by title"})
    )


class RedactorSearchForm(forms.Form):
    username = forms.CharField(
        max_length=63,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by Username"})
    )


class TopicSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by name"})
    )
