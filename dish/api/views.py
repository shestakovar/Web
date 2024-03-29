from django.shortcuts import render

# Create your views here.

from .models import Dish, Comment, Ingredient, Question, Answer
from django.contrib.auth.models import User

from rest_framework import viewsets
from .serializers import (DishSerializer, DishRetrieveSerializer,
                          IngredientSerializer,
                          CommentSerializer, CommentUpdateSerializer,
                          UserSerializer, UserUpdateSerializer,
                          QuestionSerializer, QuestionUpdateSerializer,
                          QuestionRetrieveSerializer,
                          AnswerSerializer, AnswerUpdateSerializer)
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly, IsCurrentUserOrReadOnly
from .schema import DishSchema


class HomeAPIView(viewsets.ModelViewSet):
    schema = DishSchema()
    queryset = Dish.objects.all()
    serializer_class = DishSerializer

    def get_queryset(self):
        list_dishes = self.queryset
        query = self.request.query_params.getlist('ingredient_list')
        if (len(query) != 0):
            list_dishes = list_dishes.has_ingredients(query)
        query = self.request.query_params.get('sortBy')
        if (query is not None):
            if (query == 'favs'):
                list_dishes = list_dishes.most_favs()
            elif (query == 'comments'):
                list_dishes = list_dishes.most_comments()
            else:
                list_dishes = list_dishes.alph()

        query = self.request.query_params.get('favourite')
        user = self.request.user
        if (query is not None and user is not None):
            list_dishes = list_dishes.in_bookmarks(self.request.user)

        return list_dishes

    def get_permissions(self):
        if self.request.method not in permissions.SAFE_METHODS:
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return DishRetrieveSerializer
        return DishSerializer


class CommentAPIView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [
        permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_serializer_class(self):
        if self.action == 'update':
            return CommentUpdateSerializer
        return CommentSerializer


class UserAPIView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.action == 'update':
            return UserUpdateSerializer
        return UserSerializer

    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'destroy'):
            return [permissions.IsAuthenticated(), IsCurrentUserOrReadOnly()]
        elif self.action == 'create':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]


class IngredientAPIView(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

    def get_permissions(self):
        if self.request.method not in permissions.SAFE_METHODS:
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]


class QuestionAPIView(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [
        permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_serializer_class(self):
        if self.action == 'update':
            return QuestionUpdateSerializer
        elif self.action == 'retrieve':
            return QuestionRetrieveSerializer
        return QuestionSerializer


class AnswerAPIView(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [
        permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_serializer_class(self):
        if self.action == 'update':
            return AnswerUpdateSerializer
        return AnswerSerializer
