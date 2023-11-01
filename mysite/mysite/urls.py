"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from recipeapp.views import *

from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('',recipes,name="recipes"),
    path('login/',login_page,name="login"),
    path('logout/',logout_page,name="logout"),
    path('register/',register_page,name="register"),
    path('delete-recipe/<id>/',delete_recipe,name="delete_recipe"),
    path('update-recipe/<id>/',update_recipe,name="update_recipe"),
    path('user_profile/',user_profile,name="user_profile"),
    path('recipe_full/<id>/',recipe_full,name="recipe_full"),
    path("admin/", admin.site.urls),
]


# image upload settings
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root =settings.MEDIA_ROOT)
    
urlpatterns +=staticfiles_urlpatterns()