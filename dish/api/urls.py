from django.contrib import admin
from django.urls import include, path
from .views import HomeAPIView, CommentAPIView, UserAPIView, IngredientAPIView, QuestionAPIView, AnswerAPIView

from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView

router = DefaultRouter()
router.register(r'dishes', HomeAPIView)
router.register(r'comments', CommentAPIView)
router.register(r'users', UserAPIView)
router.register(r'ingredients', IngredientAPIView)
router.register(r'questions', QuestionAPIView)
router.register(r'answers', AnswerAPIView)


urlpatterns = [
    path('openapi', get_schema_view(
        title="Your Project",
        description="API for all things …",
        version="1.0.0"
    ), name='openapi-schema'),
    path('', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
    path('', include(router.urls)),
]
