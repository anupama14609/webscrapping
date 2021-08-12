from django import forms
from django.db.models import fields
from .models import GenerateMeta, Link, WordDictionary 

class AddLinkForm(forms.ModelForm):
    class Meta:
        model= Link
        fields= ('url',)

class AddDictForm(forms.ModelForm):
    class Meta:
        model = WordDictionary
        fields = ('word',)


class GenerateMetaForm(forms.ModelForm):
    class Meta:
        model = GenerateMeta
        fields = ('url',)