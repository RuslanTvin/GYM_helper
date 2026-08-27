import input_part
def shows_dictionary_vertically(dictionary):
    for key,value in dictionary.items():
        print(str(key) + ":",value)

def convert_word_month_to_number(word_month):
    months = {
        "january": "1",
        "february": "2",
        "march": "3",
        "april":"4",
        "may": "5",
        "june": "6",
        "july": "7",
        "august": "8",
        "september": "9",
        "october": "10",
        "november": "11",
        "december":"12"
    }
    return months[word_month]

def show_one_workout_beautifully(workout_record):
    print("Date of workout",workout_record["date"],"\nExercises you did this date:")
    for exercise in workout_record["exercises"]:
        print("\nExercise name:",exercise["exercise"])
        print("\nAmount of sets you did:",exercise["sets"])
        print("\nAmount of reps you did:",exercise["reps"])
        print("\nWeight you used:",exercise["weight"])
        print("---------------------------")

def show_workout_record_from_find_function(workout_record):
    print(workout_record["date"])
    print("\nExercise name:",workout_record["exercise"]["exercise"])
    print("\nAmount of sets you did:",workout_record["exercise"]["sets"])
    print("\nAmount of reps you did:",workout_record["exercise"]["reps"])
    print("\nWeight you used:",workout_record["exercise"]["weight"])
    print("---------------------------")

def choose_workout_record(workout_records_list,list_of_progress):
    for workout_record in workout_records_list:
        show_one_workout_beautifully(workout_record)
    range_of_options = list(range(1,len(workout_records_list)+1))
    which_record = input_part.get_choice("Choose workout record.",range_of_options,False)-1
    index_of_record = list_of_progress.index(workout_records_list[which_record])
    return index_of_record

def choose_exercise_note_in_record(workout_record):
    show_one_workout_beautifully(workout_record)
    range_of_options = list(range(1,len(workout_record["exercises"])+1))
    which_note_to_update = input_part.get_choice("Choose note.",range_of_options,False)-1
    return which_note_to_update