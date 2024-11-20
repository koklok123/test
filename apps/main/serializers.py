from rest_framework import serializers

from apps.main.models import Recipe

class RecipeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Recipe
		fields = '__all__'