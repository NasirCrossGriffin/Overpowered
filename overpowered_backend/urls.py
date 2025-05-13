"""
URL configuration for overpowered_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from api import models
from api.views import CustomUserViewset, CustomExerciseViewset, CustomSetViewset, CustomWorkoutViewset
from rest_framework import routers, serializers, viewsets

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.User
        fields = ['username', 'password', 'email']

router = routers.DefaultRouter

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', CustomUserViewset.as_view()),
    path('users/<int:id>/', CustomUserViewset.as_view()),
    path('users/<str:username>/', CustomUserViewset.as_view()),
    path('workouts/', CustomWorkoutViewset.as_view()),
    path('exercises/', CustomExerciseViewset.as_view()),
    path('sets/', CustomSetViewset.as_view()),
]
