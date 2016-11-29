from django import forms
from .models import Topic, Question, Answer

class QuestionForm(forms.ModelForm):

    def as_p(self):
        "Returns this form rendered as HTML <p>s."
        return self._html_output(
            normal_row = u'<p%(html_class_attr)s>%(label)s</p> %(field)s%(help_text)s',
            error_row = u'%s',
            row_ender = '</p>',
            help_text_html = u' <span class="helptext">%s</span>',
            errors_on_separate_row = True)

    class Meta:
        model = Question
        exclude = ['author', 'q_topic_id', 'pub_date']
        #fields = ('author', 'question_text')


class AnswerForm(forms.ModelForm):

    def as_p(self):
        "Returns this form rendered as HTML <p>s."
        return self._html_output(
            normal_row = u'<p%(html_class_attr)s>%(label)s</p> %(field)s%(help_text)s',
            error_row = u'%s',
            row_ender = '</p>',
            help_text_html = u' <span class="helptext">%s</span>',
            errors_on_separate_row = True)

    class Meta:
        model = Answer
        exclude = ['author', 'a_question_topic_id', 'pub_date']
        #fields = ('author', 'answer_text')
