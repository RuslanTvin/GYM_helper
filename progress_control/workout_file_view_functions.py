import helpful_functions
def show_progress_json(list_of_progress):
    if list_of_progress:
        for workout_record in list_of_progress:
            print("______________________________")
            helpful_functions.show_one_workout_beautifully(workout_record)
    else:
        print("You dont have workout records!!!")

def find_exercise(exercise_name,list_of_progress):
    matching_exercise_notes=[]
    for workout_record in list_of_progress:
        for exercise_note in workout_record["exercises"]:
            if exercise_note["exercise"] == exercise_name:
                matching_exercise_notes.append({
        "date": workout_record["date"],
        "exercise": exercise_note
    })
    return matching_exercise_notes

def find_workout_records_with_one_date(date,list_of_progress):
    matching_records = []
    for workout_record in list_of_progress:
        if workout_record["date"] == date:
            matching_records.append(workout_record)
    return matching_records