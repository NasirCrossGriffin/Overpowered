import { React, useState, useEffect } from "react";
function CreateWorkout() {
    const [exercises, setExercises] = useState([])

    useEffect(() => {
        console.log(exercises)
    }, [exercises])

    function addExercise() {
        console.log("Add exercise accessed")

        var newExercise = {
            name : "Test Exercise",
            sets : [],
        }
        if (exercises.length > 0) {
            setExercises([...exercises, newExercise])
        } else {
            setExercises([newExercise])
        }

        console.log(exercises)
    }

    function addSet(index) {
        console.log(index)
        const thisExercise = exercises[index]
        console.log(thisExercise)
        const newSet = {
            reps : 0
        }
        if (thisExercise.sets.length > 0) {
            thisExercise.sets = [...thisExercise.sets, newSet]
        } else {
            thisExercise.sets = [newSet]
        }
        const newExercises = [...exercises]
        newExercises[index] = thisExercise
        setExercises(newExercises)
    }

    return (
        <div>
            {
                exercises.length > 0 ? exercises.map((exercise, index) => (
                    <div className="exercise" id="index">
                        <div>
                            <p>{exercise.name}</p>
                        </div>
                        {
                            exercise.sets.length > 0 ? exercise.sets.map((set, setIndex) => (
                                <div>
                                    <p>{setIndex + 1}</p>
                                    <p>{set.reps}</p>
                                </div>
                            )) : <></>
                        }
                        <button onClick={() => addSet(index)}>Add Set</button>
                    </div>
                )) : <></>
            }
            <button onClick={() => addExercise()}>Add Exercise</button>
        </div>
    )
}

export default CreateWorkout;


