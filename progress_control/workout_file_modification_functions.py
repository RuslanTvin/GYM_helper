import progress_control.dump_and_load_json
import helpful_functions
import progress_control.workout_file_view_functions
import input_part

def save_workout_progress(list_of_progress,workout_record,file_name):
    list_of_progress.append(workout_record)
    progress_control.dump_and_load_json.dump_file_with_progress_json(file_name,list_of_progress)

def delete_exercise_note_from_record(list_of_progress,file_name,date):
    workout_records_list = progress_control.workout_file_view_functions.find_workout_records_with_one_date(date,list_of_progress)
    if workout_records_list:
        index_of_record = helpful_functions.choose_workout_record(workout_records_list,list_of_progress)
        if len(list_of_progress[index_of_record]["exercises"]) > 1:
            while True:
                index_of_note = helpful_functions.choose_exercise_note_in_record(list_of_progress[index_of_record])
                list_of_progress[index_of_record]["exercises"].pop(index_of_note)
                progress_control.dump_and_load_json.dump_file_with_progress_json(file_name,list_of_progress)
                if len(list_of_progress[index_of_record]["exercises"]) == 1:
                    delete_last = input_part.get_yes_or_no("There is last exercise note in this workout record,do you want to delete it?")
                    if delete_last == "no":
                        break
                    else:    
                        list_of_progress.pop(index_of_record)
                        progress_control.dump_and_load_json.dump_file_with_progress_json(file_name,list_of_progress)
                        print("You deleted last exercise note so whole workout record will be deleted as well.")
                        break
                print("Exercise note was succesfully deleted.")
                delete_more = input_part.get_yes_or_no("would you like to delete another record(yes or no)")
                if delete_more == "no":
                    break
        else:
            list_of_progress.pop(index_of_record)
            progress_control.dump_and_load_json.dump_file_with_progress_json(file_name,list_of_progress)
            print("You deleted last exercise note so whole workout record will be deleted.")
            print("Exercise note was succesfully deleted.")
    else:
        print("There is no records with that date!!!")

def delete_workout_record(list_of_progress,date_of_workout,file_name):
    new_list_of_progress = []
    workout_records_list = progress_control.workout_file_view_functions.find_workout_records_with_one_date(date_of_workout,list_of_progress)
    if workout_records_list:
        for workout_record in list_of_progress:
            if workout_record["date"] != date_of_workout:
                new_list_of_progress.append(workout_record)
        delete_or_no = input_part.get_yes_or_no("There is "+str(len(workout_records_list))+" would you like to delete all records?(in case of 'no' you can choose wich one to delete)")
        if delete_or_no == "yes":
            progress_control.dump_and_load_json.dump_file_with_progress_json(file_name,new_list_of_progress)
        else:
            while True:
                index_of_record = helpful_functions.choose_workout_record(workout_records_list,list_of_progress)
                list_of_progress.pop(index_of_record)
                progress_control.dump_and_load_json.dump_file_with_progress_json(file_name,list_of_progress)
                workout_records_list = progress_control.workout_file_view_functions.find_workout_records_with_one_date(date_of_workout,list_of_progress)
                print("Record was succesfully deleted.")
                if workout_records_list:
                    delete_more = input_part.get_yes_or_no("would you like to delete another record(yes or no) ")
                    if delete_more == "no":
                        break
                else:
                    print("There is no more record this date.")
                    break
    else:
        print("There is no records with that date!!!")

def update_workout_note_in_record(list_of_progress,file_name,index_of_record,index_of_note,exercise_name,sets,reps,weight):
    list_of_progress[index_of_record]["exercises"][index_of_note]["exercise"] = exercise_name
    list_of_progress[index_of_record]["exercises"][index_of_note]["reps"] = reps
    list_of_progress[index_of_record]["exercises"][index_of_note]["sets"] = sets
    list_of_progress[index_of_record]["exercises"][index_of_note]["weight"] = weight
    progress_control.dump_and_load_json.dump_file_with_progress_json(file_name,list_of_progress)

    