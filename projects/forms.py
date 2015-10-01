from django import forms
from .models import ProjectComments


class CommentForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={'rows': 2}), label='Comment')

    class Meta:
        model = ProjectComments
        fields = [
            'body'
        ]