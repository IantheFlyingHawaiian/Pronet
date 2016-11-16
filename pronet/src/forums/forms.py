from django import forms
from .models import Topic, Question, Answer

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('author', 'question_text')


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('author', 'answer_text')
