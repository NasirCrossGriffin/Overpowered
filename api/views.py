from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .models import Workout
from .models import Exercise
from .models import Set
from .serializers import UserSerializer
from .serializers import WorkoutSerializer
from .serializers import ExerciseSerializer
from .serializers import SetSerializer
from datetime import datetime, timezone
import bcrypt

# Create your views here.
#User Views

class CustomUserViewset(APIView):

    def get(self, request, *args, **kwargs):
        #get a user by id and username
        user_id = kwargs.get('id')
        username = kwargs.get('username') 
        print("get view accessed") 

        if user_id:
            try:
                user = User.objects.get(id=user_id)
                userSerializer = UserSerializer(user)
                return Response(userSerializer.data, status=status.HTTP_200_OK)
            except:
                return Response({"error"}, status=status.HTTP_400_BAD_REQUEST)
        elif username:
            print("username found")
            try:
                user = User.objects.get(username=username)
                userSerializer = UserSerializer(user)
                return Response(userSerializer.data, status=status.HTTP_200_OK)
            except:
                return Response({"error"}, status=status.HTTP_400_BAD_REQUEST)
            
        print("No username or id found")
        return Response({"error"}, status=status.HTTP_400_BAD_REQUEST)
    
    def post(self, request, *args, **kwargs):
        ##Create a new user
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

        encoded_password = password.encode('utf-8')

        hashed = bcrypt.hashpw(encoded_password, bcrypt.gensalt())

        newUser = User(username = username, password = hashed, email = email)

        try:
            newUser.save()
            userSerializer = UserSerializer(newUser)
            return Response(userSerializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(str(e))
            return Response({"Cannot save this user" : str(e)}, status=status.HTTP_400_BAD_REQUEST)

#Workout Views

class CustomWorkoutViewset(APIView):

    def get(self, request, *args, **kwargs):
        #get a workout by id and name
        workout_id = kwargs.get('id')
        name = request.query_params.get('name')  

        if workout_id:
            try:
                workout = Workout.objects.get(id=workout_id)
                workoutSerializer = WorkoutSerializer(workout)
                return Response(workoutSerializer.data, status=status.HTTP_200_OK)
            except:
                return Response({"error"}, status=status.HTTP_400_BAD_REQUEST)
        elif name:
            try:
                workout = Workout.objects.get(name=name)
                workoutSerializer = WorkoutSerializer(workout)
                return Response(workoutSerializer.data, status=status.HTTP_200_OK)
            except:
                return Response({"error"}, status=status.HTTP_400_BAD_REQUEST)
            
        return Response({"error"}, status=status.HTTP_400_BAD_REQUEST)
    
    def post(self, request, *args, **kwargs):
        ##Create a new workout
        name = request.data.get('name')
        userId = request.data.get('userId')
        date = request.data.get('date')

        if (date == None):
            date = datetime.now(timezone.utc).isoformat() + 'Z'

        newWorkout = Workout(name = name, date = date, user_id = userId)

        try:
            newWorkout.save()
            workoutSerializer = WorkoutSerializer(newWorkout)
            return Response(workoutSerializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(str(e))
            return Response({"Cannot save this workout" : str(e)}, status=status.HTTP_400_BAD_REQUEST)

class CustomExerciseViewset(APIView):

    def get(self, request, *args, **kwargs):
        #get a Exercise by id and name
        exercise_id = kwargs.get('id')
        name = request.query_params.get('name')  

        if exercise_id:
            try:
                exercise = Exercise.objects.get(id=exercise_id)
                exerciseSerializer = ExerciseSerializer(exercise)
                return Response(exerciseSerializer.data, status=status.HTTP_200_OK)
            except:
                return Response({"error"}, status=status.HTTP_400_BAD_REQUEST)
        elif name:
            try:
                exercise = Exercise.objects.get(name=name)
                exerciseSerializer = ExerciseSerializer(exercise)
                return Response(exerciseSerializer.data, status=status.HTTP_200_OK)
            except:
                return Response({"error"}, status=status.HTTP_400_BAD_REQUEST)
            
        return Response({"error"}, status=status.HTTP_400_BAD_REQUEST)
    
    def post(self, request, *args, **kwargs):
        ##Create a new Exercise
        name = request.data.get('name')
        imageUrl = request.data.get('imageUrl')
        workoutId = request.data.get('workoutId')

        newExercise = Exercise(name = name, Workout_id = workoutId,  imageUrl = imageUrl)

        try:
            newExercise.save()
            exerciseSerializer = ExerciseSerializer(newExercise)
            return Response(exerciseSerializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(str(e))
            return Response({"Cannot save this exercise" : str(e)}, status=status.HTTP_400_BAD_REQUEST)

class CustomSetViewset(APIView):

    def get(self, request, *args, **kwargs):
        #get a Set by id and name
        set_id = kwargs.get('id')

        if set_id:
            try:
                set = Set.objects.get(id=set_id)
                setSerializer = SetSerializer(set)
                return Response(setSerializer.data, status=status.HTTP_200_OK)
            except:
                return Response({"error"}, status=status.HTTP_400_BAD_REQUEST)
            
        return Response({"error"}, status=status.HTTP_400_BAD_REQUEST)
    
    def post(self, request, *args, **kwargs):
        ##Create a new Set
        reps = request.data.get('reps')
        exerciseId = request.data.get('exerciseId')
        weight = request.data.get('weight')
        distance = request.data.get('distance')
        time = request.data.get('time')
        

        newSet = Set(reps = reps, exercise_id = exerciseId, weight = weight, distance = distance, time = time)

        try:
            newSet.save()
            setSerializer = SetSerializer(newSet)
            return Response(setSerializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(str(e))
            return Response({"Cannot save this set" : str(e)}, status=status.HTTP_400_BAD_REQUEST)