# Generated by Django 4.0.8 on 2023-10-30 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipeapp', '0002_alter_cuisine_name_alter_ingredientitem_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='recipe_hardness',
            field=models.CharField(default='Professional', max_length=100),
        ),
    ]
