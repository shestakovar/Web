from django import forms
from api.models import Dish, Ingredient, Comment


class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class IngredientForm(forms.Form):
    ingredient_list = forms.ModelMultipleChoiceField(Ingredient.objects.all(
    ), label="Ингредиенты", widget=forms.CheckboxSelectMultiple)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'custom-select'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
