from django.contrib import admin

# Register your models here.

from .models import Dish, Ingredient, Comment, DishIngredient, Question, Answer

admin.site.register(Dish)
admin.site.register(Ingredient)
admin.site.register(DishIngredient)
admin.site.register(Comment)
admin.site.register(Question)
admin.site.register(Answer)
