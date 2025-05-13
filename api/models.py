from django.db import models

class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    email = models.CharField(max_length=255, unique=True, default="")
    password = models.CharField(max_length=255)

class Workout(models.Model):
    name = models.CharField(max_length=255, unique=True)
    date = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class Exercise(models.Model):
    name = models.CharField(max_length=255, default="Exercise")
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE) 
    imageUrl = models.CharField(max_length=255)


class Set(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    weight = models.IntegerField(null=True)
    distance = models.IntegerField(null=True)
    time = models.IntegerField(null=True)    
    reps = models.IntegerField(null=True)

