from django import forms


class QuestionsForm(forms.Form):
    question = forms.CharField(max_length=100)


class AnswersForm(forms.Form):
    answer = forms.CharField(required=False, max_length=100)
