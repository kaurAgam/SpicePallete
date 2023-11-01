
from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages   #printing error messages
from django.contrib.auth import authenticate , login , logout #for checking correctness of password , login-> maintaiing session (in login page)
from django.core.paginator import Paginator
from .forms import RecipeForm
# Create your views here.


def recipes(request):
    
    queryset=Recipe.objects.all()
    if request.method=="POST":

        form=RecipeForm(request.POST,request.FILES)  
        
    
        data=request.POST
        recipe_User=request.user if request.user.is_authenticated else None
        recipe_image=request.FILES.get('recipe_image')
        recipe_name=data.get('recipe_name')
        recipe_description=data.get('recipe_description')
        recipe_time=data.get('recipe_time')
        recipe_hardness=data.get('recipe_hardness')
        recipe_private = data.get('recipe_private', False)

        if recipe_private == 'on':
            is_private = True
        else:
            is_private = False
        
        r=Recipe.objects.create(
            recipe_image=recipe_image,
            recipe_name=recipe_name,
            recipe_description=recipe_description,
            recipe_hardness=recipe_hardness,
            recipe_time=recipe_time,
            user=recipe_User,
            recipe_private=is_private,
        )

        if form.is_valid():
            recipe_ings = form.cleaned_data['recipe_ingredient']
            r.recipe_ingredient.set(recipe_ings)
        queryset=Recipe.objects.all()

    
    else:
        form = RecipeForm()
        

    queryset=queryset.filter(recipe_private=False).distinct()

    if request.GET.get('search'):
        queryset=(queryset.filter(recipe_name__icontains=request.GET.get('search')) | queryset.filter(recipe_description__icontains=request.GET.get('search'))).distinct()
        queryset=queryset.filter(recipe_private=False)

    #paginator starts
    paginator=Paginator(queryset,6)
    page_no=request.GET.get('page')
    querysetfinal=paginator.get_page(page_no)
    num_of_pages=querysetfinal.paginator.num_pages
    ings=ingredientItem.objects.all()
    cuis=cuisine.objects.all()
    #paginator ends

    context={
            'page':'SpicePallete Home',
            'recipes':querysetfinal, #if paginator not working change to queryset
            'numpages':num_of_pages,
            'ingredients':ings,
            'cuisines':cuis,
            'form':form,
            
            }
    return render(request,"recipeapp/recipes.html",context)

def login_page(request):

    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.info(request,'Invalid Username!')
            return redirect("/login")
        # if username does exist -> check for correctness of password
        user=authenticate(username=username, password=password)

        if user is None:
            messages.info(request,'Invalid Password!')
            return redirect("/login")
        else: # session mein add kardo
            login(request,user) #make sure you do not keep login() function name same as login_page() 
            return redirect('/')
    return render(request,"recipeapp/login.html") 

def logout_page(request):
    logout(request) #make sure you do not keep login() function name same as login_page() 
    return redirect('/')
  
def register_page(request):
    if request.method=="POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        password=request.POST.get('password')
        email=request.POST.get('email')
        
        user=User.objects.filter(username=username)
        if user.exists():
            messages.info(request,'Username already taken')
            return redirect("/register")
        
        user=User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            #passsword=password  not encrypted password
        )
        user.set_password(password) #encrypted password
        user.save()

        messages.info(request,'Account created successfully! ')
        return redirect("/login")

    return render(request,"recipeapp/register.html")

def update_recipe(request,id):
    queryset=Recipe.objects.all().get(id=id)

    if request.method=="POST":
        data=request.POST
        recipe_image=request.FILES.get('recipe_image')
        recipe_name=data.get('recipe_name')
        recipe_description=data.get('recipe_description')


        queryset.recipe_name=recipe_name
        queryset.recipe_description=recipe_description
        if recipe_image:
            queryset.recipe_image=recipe_image
        queryset.save()
        return redirect('/user_profile')
        

    context={
             'page':'update_recipe',
             'obj':queryset,
            }
    return render(request,"recipeapp/update_recipes.html",context)

def delete_recipe(request,id):
    queryset=Recipe.objects.all().get(id=id)
    queryset.delete()
    return redirect('/user_profile')

def user_profile(request):
    queryset=Recipe.objects.all()
    my_recipes=queryset.filter(user=request.user)
    num_recipes=my_recipes.count()
    private_recipes=my_recipes.filter(recipe_private=True)
    public_recipes=my_recipes.filter(recipe_private=False)
    title="MY RECIPIES"

    if request.GET.get('option_display')=='2':
        my_recipes=private_recipes
        title="PRIVATE RECIPIES"
    if request.GET.get('option_display')=='3':
        my_recipes=public_recipes    
        title="PUBLIC RECIPIES"
    context={
        'myrecipes' : my_recipes,
        'numrecipes': num_recipes,
        'title':title

    }
    return render(request, 'recipeapp/user_profile.html',context)



def recipe_full(request,id):
    queryset=Recipe.objects.all().get(id=id)
    
    context={
             'page':'recipe_full',
             'obj':queryset,
            }
    return render(request,'recipeapp/recipe_full.html',context)
