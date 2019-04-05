from django import forms
from recruitment.models import Grade


class GradeForm(forms.ModelForm):

    class Meta:
        model = Grade
        fields = ['value', 'task', 'candidate']

