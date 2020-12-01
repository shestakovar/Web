from rest_framework import serializers

from .models import Dish, Comment, Ingredient, DishIngredient, Question, Answer
from django.contrib.auth.models import User


class DishIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = DishIngredient
        fields = ('ingredient', 'weight')


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'


class DishSerializer(serializers.ModelSerializer):
    dishingredient_set = DishIngredientSerializer(many=True)
    img = serializers.ImageField(required=False)

    class Meta:
        model = Dish
        read_only_fields = ('id', 'bookmarks', 'comment_set')
        fields = ('id', 'name', 'img', 'description',
                  'dishingredient_set', 'bookmarks', 'comment_set')

    def create(self, validated_data):
        ingredients = validated_data.pop('dishingredient_set')
        dish = super().create(validated_data)
        for ingr in ingredients:
            DishIngredient.objects.create(
                dish=dish, ingredient=ingr['ingredient'], weight=ingr['weight'])
        return dish

    def update(self, instance, validated_data):
        ingredients = validated_data.pop('dishingredient_set')
        super().update(instance, validated_data)
        old = DishIngredient.objects.filter(dish=instance).delete()
        for ingr in ingredients:
            DishIngredient.objects.create(
                dish=instance, ingredient=ingr['ingredient'], weight=ingr['weight'])
        return instance


class CommentSerializer(serializers.ModelSerializer):
    current_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Comment
        read_only_fields = ('date', 'author')
        fields = '__all__'

    def create(self, validated_data):
        validated_data['author'] = validated_data.pop('current_user')
        return super().create(validated_data)


class CommentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('content',)


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        read_only_fields = ('dish_set',)
        fields = ('username', 'password', 'dish_set')

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserUpdateSerializer(UserSerializer):
    class Meta:
        model = User
        fields = ('password', 'dish_set')

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        read_only_fields = ('date', 'author')
        fields = '__all__'
        
        current_user = serializers.HiddenField(
            default=serializers.CurrentUserDefault()
        )

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        read_only_fields = ('author', 'question')
        fields = '__all__'
        
        current_user = serializers.HiddenField(
            default=serializers.CurrentUserDefault()
        )
