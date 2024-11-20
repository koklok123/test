from django.db import models

# Create your models here.
class Recipe(models.Model):
	recipe = models.CharField(max_length=225,
	verbose_name='Название рецепта')
	
	name_ingredients = models.TextField(verbose_name='Название ингридентов')

	instructions = models.TextField(verbose_name='Инструкции')

	cooking_time = models.TextField(verbose_name='Время приголовления')

	#Если вегеториянский то True
	status = models.BooleanField(verbose_name='Веганское ли блюдо?',
							   default=False)

	creation_date = models.DateField(verbose_name='Дата создания',
								  auto_now_add=True)
	