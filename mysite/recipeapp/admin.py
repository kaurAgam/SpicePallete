
from django.contrib import admin
from .models import ingredientItem, cuisine, Recipe

# Register your models with the admin site
@admin.register(ingredientItem)
class IngredientItemAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(cuisine)
class CuisineAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('recipe_name', 'recipe_hardness', 'recipe_time', 'recipe_cuisine')
    list_filter = ('recipe_hardness', 'recipe_cuisine')
    search_fields = ('recipe_name', 'recipe_description')
    filter_horizontal = ('recipe_ingredient',)  # For easier selection of ingredients

    # Customize the form for adding/editing a recipe
    fieldsets = (
        ('Recipe Details', {
            'fields': ('user', 'recipe_name', 'recipe_description', 'recipe_image', 'recipe_cuisine', 'recipe_ingredient')
        }),
        ('Additional Information', {
            'fields': ('recipe_view_count', 'recipe_hardness', 'recipe_time'),
        }),
    )
