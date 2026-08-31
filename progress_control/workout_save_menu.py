import progress_control.dump_and_load_json
import input_part
import progress_control.workout_file_modification_functions
import progress_control.workout_file_view_functions
import progress_control.output_for_user_options
def workout_save_menu(list_of_progress,numeral_system)->str:
    FILE_NAME="progress.json"
    option=input_part.get_choice("Here are your options.\n1:Save new workout.\n2:Check every workout record.\n3:Find exercise or workout records.\n4:Delete menu.\n5:Update specific exercise.\n6:Exit back to main menu. ",[1,2,3,4,5,6],False)
    if option == 1:
        progress_control.output_for_user_options.workout_save_option(FILE_NAME,list_of_progress,numeral_system)

    elif option == 2:

        progress_control.workout_file_view_functions.show_progress_json(list_of_progress)
        
    elif option == 3:
        progress_control.output_for_user_options.find_exercise_option(list_of_progress)

    elif option == 4:
        
        progress_control.output_for_user_options.delete_exercise_or_record_option(list_of_progress,FILE_NAME)
        
    elif option == 5:

        progress_control.output_for_user_options.update_option(list_of_progress,FILE_NAME,numeral_system)
    elif option == 6:
        pass