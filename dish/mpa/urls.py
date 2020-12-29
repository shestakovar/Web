from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.HomeListView.as_view(), name='home'),
    path('find', views.FindListView.as_view(), name='find'),
    path('detail/<int:pk>', views.HomeDetailView.as_view(), name='detail_page'),
    path('accounts/register', views.RegisterCreateView.as_view(), name='register'),
    path('add_remove_bookmark/<int:pk>',
         views.add_remove_bookmark, name='add_remove_bookmark'),
    path('favourites', views.FavouriteListView.as_view(), name='favourites'),
    path('questions', views.QuestionsListView.as_view(), name='questions'),
    path('questions/<int:pk>', views.QuestionsDetailView.as_view(), name='question_detail_page')
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
