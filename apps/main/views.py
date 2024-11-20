from django.shortcuts import render
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.pagination import PageNumberPagination
from apps.main.models import Recipe
from apps.main.serializers import RecipeSerializer

# Create your views here.


class Pagination(PageNumberPagination):
    page_size = 3
    max_page_size = 10

class RecipeAPI(GenericViewSet,
              mixins.ListModelMixin,
              mixins.CreateModelMixin,
              mixins.RetrieveModelMixin,
              mixins.UpdateModelMixin,
              mixins.DestroyModelMixin):
    
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    pagination_class = Pagination