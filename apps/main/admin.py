from django.contrib import admin
from apps.main.models import Recipe
# Register your models here.

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
	list_display = ['recipe', 'name_ingredients', 'instructions', 'cooking_time', 'status', 'creation_date']
