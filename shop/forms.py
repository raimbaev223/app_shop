
from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
#
# class CommentForm(forms.Form):
#     author = forms.CharField(
#         max_length=60,
#         widget=forms.TextInput(
#             attrs={"class": "form-control", "placeholder": "Ваше имя"}
#         ),
#     )
#     body = forms.CharField(
#         widget=forms.Textarea(
#             attrs={"class": "form-control", "placeholder": "Оставить отзыв!"}
#         )
#     )