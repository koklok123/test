from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.main.views import RecipeAPI

router = DefaultRouter()
router.register("api_news", RecipeAPI, basename='api-news')

urlpatterns = [

]

urlpatterns += router.urls