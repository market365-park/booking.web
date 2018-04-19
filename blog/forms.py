# -*- encoding: utf-8 -*-
from django import forms

from .models import Post


class PostSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word')

class PostForm(forms.ModelForm):
    title = forms.CharField(
        label="Title ",
        max_length=60,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '제목을 입력하세요.(70글자 제한)',
                'required': 'true',
            }))

    content = forms.CharField(
        label="Content ",
        max_length=300,
        help_text="Required. 300 characters or fewer.",
        error_messages={
            'invalid': "에허허허"},
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': '내용을 입력하세요.(300글자 제한)',
                'required': 'true',
            }))

    class Meta:
        model = Post
        fields = ("title", "content")