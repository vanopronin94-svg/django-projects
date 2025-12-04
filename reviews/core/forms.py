from django import forms
from core.models import ReviewModel
class ReviewForm(forms.ModelForm):
    class Meta:
        model=ReviewModel
        fields=["name","email","review","rating"]
        widgets={"rating":forms.NumberInput(attrs={"min":1,"max":5})}