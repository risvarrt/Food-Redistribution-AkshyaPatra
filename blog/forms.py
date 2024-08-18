from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['Name','Required_Quantity']


class CommentForm1(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['Name']