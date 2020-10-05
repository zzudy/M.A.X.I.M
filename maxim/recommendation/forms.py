from django import forms

from .models import Request, RecommendationRequest

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ('subjectName', 'level', 'day', 'time',)

class RecommendationRequestForm(forms.ModelForm) :
    class Meta : 
        model = RecommendationRequest
        fields = ('selected_class',)