from django import forms
from .models import Post, Comment, Category, Report

choices = Category.objects.all().values_list("name", "name")
choices_list = []

for item in choices:
    choices_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "album", "singer", "header_image", "category", "audio")
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control"}),
            'singer': forms.TextInput(attrs={"class": "form-control"}),
            'album': forms.TextInput(attrs={"class": "form-control"}),
            'category': forms.Select(choices=choices_list, attrs={"class": "form-control"}),
            'audio': forms.FileInput(attrs={"class": "form-control"}),
            # 'header_image': forms.ImageField(attrs={"class": "form-control"}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['text']
