from rest_framework import serializers
from .models import User
from .models import Workout
from .models import Exercise
from .models import User_Exercise
from .models import Set

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # Include the fields you want to return in the API
        fields = ['id', 'username', 'email']

class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        # Include the fields you want to return in the API
        fields = ['name', 'date', 'user']

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        # Include the fields you want to return in the API
        fields = ['name', 'imageUrl']

class UserExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Exercise
        # Include the fields you want to return in the API
        fields = ['workout', 'exercise']

class SetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Set
        # Include the fields you want to return in the API
        fields = ['user_exercise', 'reps', 'weight', 'distance', 'time']