# Generated by Django 4.0.8 on 2023-10-30 14:36

from django.db import migrations, models
import recipeapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('recipeapp', '0003_alter_recipe_recipe_hardness'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='recipe_cuisine',
            field=models.CharField(blank=True, default='earth', max_length=50, verbose_name=recipeapp.models.cuisine),
        ),
    ]
