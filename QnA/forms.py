from django import forms

class QuestionForm(forms.Form):
    question_text = forms.CharField(label='Your Question', max_length=100)
