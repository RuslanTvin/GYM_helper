import progress_control.workout_file_view_functions
import datetime
import input_part
import progress_control.workout_file_modification_functions
import helpful_functions

def workout_save_option(FILE_NAME,list_of_progress):
    day_of_record = str(datetime.date.today())
    
    specific_date_of_user = input_part.get_yes_or_no("Would you like to save workout of date you choose?(In case of 'no' today`s date will be used) ")
    
    if specific_date_of_user == "yes" or specific_date_of_user == "y":
        day_of_record = input_part.get_date()

    record_note = {"date":day_of_record,
             "exercises":[
             ]
             }
    record_note = input_part.add_exercise_note_for_one_workout(record_note)
    
    progress_control.workout_file_modification_functions.save_workout_progress(list_of_progress,record_note,FILE_NAME)
    
    print("Your progress saved successfully!")

def find_exercise_option(list_of_progress):
    if list_of_progress:
        date_or_exercise_name = input_part.get_choice("You want to:\n1:Find all exercises with one name\n2:find all workout record with one date(please enter 1 or 2): ",[1,2],False)
        if date_or_exercise_name == 1:
            exercise_name=input_part.get_string("What exercise you looking for?")
            list_of_matching_workouts=progress_control.workout_file_view_functions.find_exercise(exercise_name,list_of_progress)
            if len(list_of_matching_workouts) > 0:
                for record in list_of_matching_workouts:
                    print("-----------------------")
                    print(record["date"])
                    helpful_functions.shows_dictionary_vertically(record["exercise"])
                    print("-----------------------")
            else:
                print("There is no exercises with that name!!!")
        else:
            specific_date = input_part.get_date()
            list_of_matching_workout_records = progress_control.workout_file_view_functions.find_workout_records_with_one_date(specific_date,list_of_progress)
            if  len(list_of_matching_workout_records) > 0:
                progress_control.workout_file_view_functions.show_progress_json(list_of_matching_workout_records)
            else:
                print("You dont have any workout record with that date.You can check every workout record by option 2!!!")
    else:
        print("You dont have any workout record yet!!!")

def delete_exercise_or_record_option(list_of_progress,file_name):
    print("You are in delete menu.")
    what_to_delete = input_part.get_choice("1:Delete whole record/records for one date\n2:Delete exericse note in workout record ",[1,2],False)
    if what_to_delete == 1:
        date = input_part.get_date()
        progress_control.workout_file_modification_functions.delete_workout_record(list_of_progress,date,file_name)
    elif what_to_delete == 2:
        date = input_part.get_date()
        progress_control.workout_file_modification_functions.delete_exercise_note_from_record(list_of_progress,file_name,date)

def update_option (list_of_progress,file_name):
    date = input_part.get_date()
    workout_records_list = progress_control.workout_file_view_functions.find_workout_records_with_one_date(date,list_of_progress)
    if len(workout_records_list) > 0:
        index_of_record = helpful_functions.choose_workout_record(workout_records_list,list_of_progress)
        while True:
            which_note_to_update = helpful_functions.choose_exercise_note_in_record(list_of_progress[index_of_record])
            exercise_name, sets, reps, weight = input_part.get_workout_data_with_exercise_name()
            progress_control.workout_file_modification_functions.update_workout_note_in_record(list_of_progress,file_name,index_of_record,which_note_to_update,exercise_name,sets,reps,weight)
            print("Exercise note was succesfully updated.")
            update_another = input_part.get_yes_or_no("Do you want to edit another exercise note?(yes or no)")
            workout_records_list = progress_control.workout_file_view_functions.find_workout_records_with_one_date(date,list_of_progress)
            if update_another == "no":
                break
    else:
        print("There is no records with that date!!!")