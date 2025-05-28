# Class definition for Set class, includes attributes namely the weight, 
# the reps, and the rest time between each set

class Set: 

    # REQUIRES: int weight, int reps, int rest 
    # EFFECTS: creates a set object that has a given weight, reps and rest time 

    def __init__(self, weight, reps, rest):
        self.weight = weight
        self.reps = reps
        self.rest = rest
        
    # Setters and getters below

    def getWeight(self):
        return self.weight
    
    def getReps(self):
        return self.reps
    
    def getRest(self):
        return self.rest
    
    def setWeight(self, weightNew):
        self.weight = weightNew
    
    def setReps(self, repsNew):
        self.reps = repsNew
    
    def setRest(self, restNew):
        self.rest = restNew


