from django.shortcuts import render, redirect

# Create your views here.

from api.models import Dish, Comment, Ingredient, Question
from django.views.generic import ListView, DetailView, CreateView
from .forms import DishForm, IngredientForm, CommentForm, QuestionForm, AnswerForm
from django.urls import reverse, reverse_lazy

from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from api.managers import DishManager


class HomeListView(ListView):
    model = Dish
    template_name = 'home.html'
    context_object_name = 'list_dishes'

    def get_queryset(self):
        query = self.request.GET.get('sortBy')
        if (query == 'favs'):
            return self.model.objects.most_favs()
        elif (query == 'comments'):
            return self.model.objects.most_comments()
        else:
            return self.model.objects.alph()


class FindListView(HomeListView):
    template_name = 'find.html'

    def get_queryset(self):
        list_dishes = []
        self.form = IngredientForm
        if self.request.GET:
            form = IngredientForm(self.request.GET)
            if form.is_valid():
                self.form = form
                temp = self.form.cleaned_data.get('ingredient_list')
                list_dishes = self.model.objects.has_ingredients(temp)

                query = self.request.GET.get('sortBy')
                if (query == 'favs'):
                    list_dishes = list_dishes.most_favs()
                elif (query == 'comments'):
                    list_dishes = list_dishes.most_comments()
                else:
                    list_dishes = list_dishes.alph()

        return list_dishes

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form
        return context


class FavouriteListView(LoginRequiredMixin, HomeListView):
    template_name = 'favourites.html'

    def get_queryset(self):
        return super().get_queryset().in_bookmarks(self.request.user)


class HomeDetailView(DetailView):
    model = Dish
    template_name = 'detail.html'
    context_object_name = 'dish'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm
        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.article = self.get_object()
            obj.author = request.user
            obj.save()
            form = CommentForm

        self.object = self.get_object()
        context = super().get_context_data(**kwargs)
        context['form'] = form
        return self.render_to_response(context=context)


class RegisterCreateView(CreateView):
    model = User
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form_valid = super().form_valid(form)
        name = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        auth = authenticate(username=name, password=password)
        login(self.request, auth)
        return form_valid


@login_required
def add_remove_bookmark(request, pk):
    if request.method == 'POST':
        dish_obj = Dish.objects.get(pk=pk)
        if request.user in dish_obj.bookmarks.all():
            dish_obj.bookmarks.remove(request.user)
        else:
            dish_obj.bookmarks.add(request.user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class QuestionsListView(ListView):
    model = Question
    template_name = 'questions.html'
    context_object_name = 'list_questions'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = QuestionForm
        return context

    def post(self, request, *args, **kwargs):
        form = QuestionForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj.save()
            form = QuestionForm

        self.object_list = self.get_queryset()
        context = super().get_context_data(**kwargs)
        context['form'] = form
        return self.render_to_response(context=context)


class QuestionsDetailView(DetailView):
    model = Question
    template_name = 'question_detail.html'
    context_object_name = 'question'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AnswerForm
        return context

    def post(self, request, *args, **kwargs):
        form = AnswerForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.question = self.get_object()
            obj.author = request.user
            obj.save()
            form = AnswerForm

        self.object = self.get_object()
        context = super().get_context_data(**kwargs)
        context['form'] = form
        return self.render_to_response(context=context)
