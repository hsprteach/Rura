from django import forms
from .models import Learner

class LearnerDetail(forms.ModelForm):
    class Meta:
        model = Learner
        fields = '__all__'
        