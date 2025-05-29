import Set

# Class used to represent an Exercise. Contains features regarding to a specific exercise 
# like list of sets, number of sets, personal best, total time for exercise etc. 

class Exercise: 

    def __init__(self, name, time):
        self.time = time
        self.name
        self.sets = []
        self.personalBest = 0
        self.numberSets = 0
    
    # REQUIRES: int weight > 0, int reps > 0, int rest > 0 (future update to use a try catch)
    # MODIFIES: this
    # EFFECTS: adds a set with given weight, reps and rest
    def addSet(self, weight, reps, rest): 
        newSet = Set(weight, reps, rest)
        self.sets.append(newSet)
        self.numberSets += 1 
        updatePersonalBest(weight)

    # MODIFIES: this
    # EFFECTS: removes the last set from the list of exercises
    def removeSet(self):
        self.sets.pop()
        self.numberSets -= 1
        # TODO: should there be a code to update personal best ? 

    # REQUIRES: int setNumber in [1, numberSets], int weight > 0, int reps > 0, int rest > 0 (future update to use a try catch)
    # MODIFIES: this
    # EFFECTS: modifies a given set with given weight, reps and rest
    def modifySet(self, setNumber, weight, reps, rest): 
        newSet = Set(weight, reps, rest)
        self.sets[setNumber - 1] = newSet 
        updatePersonalBest(weight)

    # MODIFIES: this
    # EFFECTS: Updates the personal best value is weight > personalBest
    def updatePersonalBest(self, weight):
        if weight > self.personalBest: 
            self.personalBest = weight
        
    # GETTERS AND SETTERS BELOW: 
    
    def getPersonalBest(self):
        return self.personalBest
    
    def getNumberSets(self): 
        return self.numberSets

    def getTime(self): 
        return self.time

    def getSets(self):
        return self.sets

    def getExerciseName(self):
        return self.name

    def setName(self, name): 
        self.name = name
        
    def setPersonalBest(self, weight): 
        self.personalBest = weight
    
    def setTime(self, time):
        self.time = time