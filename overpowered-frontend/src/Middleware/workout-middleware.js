async function getWorkoutById(workoutId) {
    const workout = await fetch(`http://localhost:3001/workouts/${workoutId}/`,
        {
            method : "GET",
            headers : {"Content-Type" : "application/json"},
            credentials : true
        }
    );

    if (workout.ok) {
        return workout;
    }

    return null;
}

async function getWorkoutByName(name) {
    const workout = await fetch(`http://localhost:3001/workouts/${name}/`,
        {
            method : "GET",
            headers : {"Content-Type" : "application/json"},
            credentials : true
        }
    );
t
    if (workout.ok) {
        return workout;
    }

    return null;
}

async function createWorkout(protoWorkout) {
    const workout = await fetch(`http://localhost:3001/workouts/`,
        {
            method : "POST",
            body : JSON.stringify(protoWorkout),
            headers : {"Content-Type" : "application/json"},
            credentials : true
        }
    );

    if (workout.ok) {
        return workout;
    }

    return null;
}