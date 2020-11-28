from django.contrib import admin
from django.urls import include, path
from .views import HomeAPIView, CommentAPIView, UserAPIView, IngredientAPIView

from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView

router = DefaultRouter()
router.register(r'dishes', HomeAPIView)
router.register(r'comments', CommentAPIView)
router.register(r'users', UserAPIView)
router.register(r'ingredients', IngredientAPIView)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('openapi', get_schema_view(
        title="Your Project",
        description="API for all things …",
        version="1.0.0"
    ), name='openapi-schema'),
    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
]
