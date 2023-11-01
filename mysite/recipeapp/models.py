from django.db import models
from django.contrib.auth.models import User



class ingredientItem(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self): 
        return self.name

class cuisine(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self): 
        return self.name

class Recipe(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True)  #SET_DEFAULT : default vales are written SET_NULL using this instead of getting deleted we get NULL values
    
    recipe_name=models.CharField(max_length=100)
    recipe_description=models.TextField()
    recipe_image=models.ImageField(upload_to="images_db")
    recipe_view_count=models.IntegerField(default=0)
    
    recipe_hardness=models.CharField(max_length=100,default='Professional')
    recipe_time=models.IntegerField(default=60, blank=True, null=True) #amount of time in minutes
    
    recipe_cuisine=models.CharField(cuisine,blank=True, default='earth',max_length=50)

    recipe_ingredient = models.ManyToManyField(ingredientItem,  blank=True)
    recipe_private=models.BooleanField(default=False)