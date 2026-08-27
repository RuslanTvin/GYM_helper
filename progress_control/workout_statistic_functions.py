
def total_number_of_workout_records(list_of_progress):
    total_number_of_workout_records = len(list_of_progress)
    return total_number_of_workout_records

def total_number_of_exercises(list_of_progress):
    total_number_of_exercises = 0
    for workout_record in list_of_progress:
        total_number_of_exercises += len(workout_record["exercises"])
    return total_number_of_exercises 

def total_number_of_unique_exercises(list_of_progress):
    list_of_unique_exercises = []
    for workout_record in list_of_progress:
        for exercise in workout_record["exercises"]:
            if exercise["exercise"] not in list_of_unique_exercises:
                list_of_unique_exercises.append(exercise["exercise"])
    return len(list_of_unique_exercises)

def maximum_for_something(list_of_exercise_notes,maximum_of_what):
    maximum_value = 0
    for exercise_note in list_of_exercise_notes:
        if exercise_note["exercise"][maximum_of_what] > maximum_value:
            maximum_value = exercise_note["exercise"][maximum_of_what]
    return maximum_value

def average_of_something(list_of_exercise_notes,average_of_what):
    values = []
    for exercise_note in list_of_exercise_notes:
        values.append(exercise_note["exercise"][average_of_what])
    sum_of_values = sum(values)
    return sum_of_values / len(values)

def sort_exercises_list_by_dates(list_of_exercise_notes):
    sorted_list = sorted(list_of_exercise_notes, key=lambda x : x["date"])
    return sorted_list

def sort_exercises_list_by_weight(list_of_exercise_notes,reverse):
    sorted_list = sorted(list_of_exercise_notes, key=lambda x : x["exercise"]["weight"],reverse=reverse)
    return sorted_list