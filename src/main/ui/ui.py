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

    # function to view all workouts and interact with them
    def viewWorkouts(self): 
        for i in range(len(self.workoutList)): 
            print(f"{i + 1}. {self.workoutList[i].getName()}")

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
