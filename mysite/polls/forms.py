from django import forms
from .models import Question, Choice

class PostForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('question_text',) 
