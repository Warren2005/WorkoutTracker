import streamlit as st
from src.main.model.Exercise import Exercise
from src.main.model.Workout import Workout

# Initialize workout list in session state
if "workout_list" not in st.session_state:
    st.session_state.workout_list = []

st.title("🏋️ Workout Tracker")
st.markdown("Track your workouts, exercises, and sets with ease!")

# Create Workout
st.sidebar.header("➕ Create New Workout")
new_workout_name = st.sidebar.text_input("Workout Name")
if st.sidebar.button("Create Workout"):
    if new_workout_name:
        st.session_state.workout_list.append(Workout(new_workout_name))
        st.sidebar.success(f"Workout '{new_workout_name}' added!")
    else:
        st.sidebar.error("Workout name cannot be empty.")

# Workout Selection
st.header("📋 Your Workouts")
if st.session_state.workout_list:
    workout_names = [w.getName() for w in st.session_state.workout_list]
    selected_workout_name = st.selectbox("Choose a workout to view/edit:", workout_names)
    selected_workout = next(w for w in st.session_state.workout_list if w.getName() == selected_workout_name)

    # Remove Workout
    if st.button("🗑️ Remove This Workout"):
        st.session_state.workout_list.remove(selected_workout)
        st.success(f"Removed workout '{selected_workout_name}'")
        st.experimental_rerun()

    st.subheader(f"🏃 Exercises in '{selected_workout.getName()}'")

    # List Exercises
    for exercise in selected_workout.getExercises():
        with st.expander(f"💪 {exercise.getName()}"):
            sets = exercise.getSets()
            if sets:
                for i, s in enumerate(sets, 1):
                    st.write(f"**Set {i}** - Weight: {s.getWeight()}kg | Reps: {s.getReps()} | Rest: {s.getRest()}s")

            # Add Set
            with st.form(f"add_set_{exercise.getName()}"):
                st.write("➕ Add a Set")
                weight = st.number_input("Weight (kg)", min_value=0)
                reps = st.number_input("Reps", min_value=0)
                rest = st.number_input("Rest (seconds)", min_value=0)
                submitted_set = st.form_submit_button("Add Set")
                if submitted_set:
                    exercise.addSet(weight, reps, rest)
                    st.success("Set added!")
                    st.experimental_rerun()

            # Remove last set
            if st.button(f"Remove Last Set - {exercise.getName()}"):
                if sets:
                    sets.pop()
                    st.warning("Last set removed.")
                    st.experimental_rerun()
                else:
                    st.info("No sets to remove.")

    # Add Exercise
    st.subheader("➕ Add a New Exercise")
    with st.form("add_exercise_form"):
        exercise_name = st.text_input("Exercise Name")
        time_taken = st.number_input("Time Taken (minutes)", min_value=0)
        submitted_exercise = st.form_submit_button("Add Exercise")
        if submitted_exercise:
            if exercise_name:
                selected_workout.addExercise(exercise_name, time_taken)
                st.success(f"Exercise '{exercise_name}' added to workout!")
                st.experimental_rerun()
            else:
                st.error("Exercise name cannot be empty.")
else:
    st.info("You haven't added any workouts yet.")
