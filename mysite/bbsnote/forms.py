from django import forms
from bbsnote.models import Board

class BoardForm(forms.ModelForm) :
    class Meta :
        model=Board
        fields=['subject', 'content']
        labels={
            'subject' : '제목',
            'content' : '내용',
        }