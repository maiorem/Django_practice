from django import forms
from bbsnote.models import Board

class BoardForm(forms.ModelForm) :
    class Meta :
        model=Board
        fields=['subject', 'content']