from src.main.model.Exercise import Exercise
from src.main.model.Workout import Workout





class UserInterface: 
    
    def __init__(self):
        self.workoutList = []                        

    # function to create a workout            
    def createWorkout(self):
        name = input("Enter the name of the workout: ")
        workout = Workout(name)  # Make sure Workout is imported
        self.workoutList.append(workout)

    # function to add new exercise
    def addNewExercise(self, workout): 
        name = input("Enter the name of the exercise: ")
        time = int(input("Enter the time taken to complete the exercise in mins: "))
        workout.addExercise(name, time)

    # function to display exercises
    def displayExercises(self, workout):
        exerciseList = workout.getExercises()
        for i in range(len(exerciseList)): 
            print(f"{i + 1}. {exerciseList[i].getName()}")
        
        print() 
        print("\nMenu:")
        print("a. Add an Exercise")
        print("b. Remove the Last Exercie")
        # print("c. Modify an Exercise")
        print("q. Exit")

        while True:
            user_input = input("Enter your choice: ").strip()

            if user_input == "a": 
                self.addNewExercise(workout)
            elif user_input == "b": 
                exerciseList = workout.getExercises()
                if exerciseList: 
                    removed = exerciseList.pop()
                    print(f"Removed: {removed.getName()}")
                else: 
                    print("No exercises to remove.")
            # elif user_input == "c": 
            #     num = int(input("Enter the number by the side of the exercise"))
            #     exerciseList = workout.getExercises()
            #     exercise = exerciseList[num - 1]
            #     self.displaySets(exercise)
            elif user_input == "q":
                print("Exiting...")
                break
            else:
                print("Invalid input. Try again.")

    # function to view all workouts and interact with them
    def viewWorkouts(self): 
        for i in range(len(self.workoutList)): 
            print(f"{i + 1}. {self.workoutList[i].getName()}")
        
        num = int(input("Press the number by the workout to view its details")) #num should be in allowed range

        while True:
            workout = self.workoutList[num - 1]

            if (len(workout.getExercises()) == 0): 
                print("Please add an Exercise:")
                self.addNewExercise(workout)
            else: 
                self.displayExercises(workout)
                break
            


    # function to run the app 
    def run(self): 
        while True: 
            # if Workout List is empty, prompt user to enter a workout
            if len(self.workoutList) == 0: 
                print("Please create your first workout: ")
                self.createWorkout()

            else:
                print("\nMenu:")
                print("1. Add a Workout")
                print("2. Remove the Last Workout")
                print("3. View All Workouts")
                print("q. Exit")

                user_input = input("Enter your choice: ").strip()

                if user_input == "1": 
                    self.createWorkout()
                elif user_input == "2": 
                    if self.workoutList: 
                        removed = self.workoutList.pop()
                        print(f"Removed: {removed.getName()}")
                    else: 
                        print("No workouts to remove.")
                elif user_input == "3": 
                    self.viewWorkouts()
                elif user_input == "q":
                    print("Exiting...")
                    break
                else:
                    print("Invalid input. Try again.")



ui = UserInterface()
ui.run()
