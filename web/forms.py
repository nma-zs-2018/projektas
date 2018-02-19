from django import forms

class QuestionsForm(forms.Form):
    question = forms.CharField(label='Question', max_length=100)

class AnswersForm(forms.Form):
    answer = forms.CharField(label='Answer', max_length=100)