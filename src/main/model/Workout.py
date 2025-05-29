import Exercise 
import Set 


# Class to represent a workout, with its name and list of exercises performed

class Workout:

    def __init__(self, name): 
        self.name = name 
        self.exercises = []
        self.numExercises = 0

    # REQUIRES: name be a nonempty string, time > 0
    # MODIFIES: this or (self)
    # EFFECTS: adds a new exercise to the list of exercises
    def addExercise(self, name, time):
        newExercise = Exercise(name, time)
        self.exercises.append(newExercise)
        self.numExercises += 1

    # REQUIRES: self.exercises be non-empty, exerciseNum in [1, len(self.exercises)] (USE Try-catch for exerciseNum index out of bounds)
    # MODIFIES: this or (self)
    # EFFECTS: removes the exercise with index = exerciseNum - 1
    def removeExercise(self, exerciseNum): 
        if (len(self.exercises) > 0): 
            self.exercises.remove(exerciseNum - 1)
            self.numExercises -= 1

    # REQUIRES: exerciseNum in [1, len(self.exercises)], name must be a non-empty string, time > 0
    # MODIFIES: this or (self)
    # EFFECTS: modifies an exercise weith index (exerciseNum - 1)
    def modifyExercise(self, exerciseNum, name, time): 
        newExercise = Exercise(name, time)
        self.exercises[exerciseNum - 1] = newExercise 

    # GETTERS and SETTERS below

    def getName(self): 
        return self.name 
    
    def getExercises(self): 
        return self.exercises 

    def getNumExercises(self): 
        return self.numExercises

    def setName(self, name): 
        self.name = name
    
    