
from django import forms
from .models import Recipe



class RecipeForm(forms.ModelForm):
  
    date_published = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    
    class Meta:
        model = Recipe
        fields ='__all__'
        exclude = ('likes', 'uploaded_date', 'updated',)
      
class RawRecipeForm(forms.Form):
    class Meta:
      model = Recipe
      fields ='__all__'
