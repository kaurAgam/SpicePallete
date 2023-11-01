from django import forms
from .models import Recipe, ingredientItem,cuisine
from django.contrib.auth.forms import UserCreationForm

class RecipeForm(forms.ModelForm):
    # recipe_cuisine = forms.ModelChoiceField(
    #     queryset=cuisine.objects.all().order_by('name'),)
    class Meta:
        model = Recipe
        fields = [ 'recipe_ingredient']

