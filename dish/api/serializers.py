from rest_framework import serializers

from .models import Dish, Comment, Ingredient, DishIngredient, Question, Answer
from django.contrib.auth.models import User


class DishIngredientSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='ingredient.name', read_only=True)

    class Meta:
        model = DishIngredient
        fields = ('ingredient', 'weight', 'name')


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'


class DishSerializer(serializers.ModelSerializer):
    dishingredient_set = DishIngredientSerializer(many=True)
    img = serializers.ImageField(required=False)

    class Meta:
        model = Dish
        read_only_fields = ('id', 'bookmarks')
        fields = ('id', 'name', 'img', 'description',
                  'dishingredient_set', 'bookmarks')

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


class CommentForDishSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        read_only_fields = ('date', 'author')
        fields = ('id', 'content', 'date', 'author')


class DishRetrieveSerializer(DishSerializer):
    comment_set = CommentForDishSerializer(many=True)

    class Meta:
        model = Dish
        read_only_fields = ('id', 'bookmarks', 'comment_set')
        fields = ('id', 'name', 'img', 'description',
                  'dishingredient_set', 'bookmarks', 'comment_set')


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


class DishForUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dish
        read_only_fields = ('id', 'name')
        fields = ('id', 'name')


class UserBasicSerializer(serializers.ModelSerializer):
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


class UserSerializer(UserBasicSerializer):
    password = serializers.CharField(write_only=True)
    dish_set = DishForUserSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'dish_set')


class UserUpdateSerializer(UserBasicSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('password', 'dish_set')


class QuestionSerializer(serializers.ModelSerializer):
    current_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Question
        read_only_fields = ('date', 'author')
        fields = '__all__'

    def create(self, validated_data):
        validated_data['author'] = validated_data.pop('current_user')
        return super().create(validated_data)


class AnswerForQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'content', 'author', 'date')


class QuestionRetrieveSerializer(serializers.ModelSerializer):
    answer_set = AnswerForQuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ('title', 'content', 'author', 'date', 'answer_set')


class QuestionUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('content',)


class AnswerSerializer(serializers.ModelSerializer):
    current_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Answer
        read_only_fields = ('author', 'date')
        fields = '__all__'

    def create(self, validated_data):
        validated_data['author'] = validated_data.pop('current_user')
        return super().create(validated_data)


class AnswerUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('content',)
