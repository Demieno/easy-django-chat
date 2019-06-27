from django import forms
from .models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = "__all__"

    body = forms.CharField(label='Введите текст', widget=forms.Textarea(attrs={'class': 'materialize-textarea'}))
